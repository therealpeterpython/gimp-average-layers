#!/usr/bin/env python
from gimpfu import *
from array import array
import time
import sys

import itertools
import operator

from collections import Counter

# Not sure if get_mode() or get_mode1() is faster
# but it looks like get_mode is despite its length the faster one

def get_mode1(lst):
    return Counter(lst).most_common(1)[0][0]


# Returns the mode of the list
def get_mode(lst):
    # get an iterable of (item, iterable) pairs
    SL = sorted((x, i) for i, x in enumerate(lst))
    groups = itertools.groupby(SL, key=operator.itemgetter(0))
    # auxiliary function to get "quality" for an item
    def _auxfun(g):
        item, iterable = g
        count = 0
        min_index = len(lst)
        for _, where in iterable:
            count += 1
            min_index = min(min_index, where)
        # print 'item %r, count %r, minind %r' % (item, count, min_index)
        return count, -min_index
    # pick the highest-count/earliest item
    return max(groups, key=_auxfun)[0]


# Returns the median of the list as input type if the list has an odd length
# or the mean between the two middle elements as float
def get_median(lst):
    n = len(lst)
    h = n//2
    lst.sort()
    if n % 2:
            return lst[h]
    else:
            return sum(lst[h-1:h+1])/2.0


# Returns the mean of the list as float
def get_mean(list):
    return sum(list) / float(len(list))


# Returns the visible layers of the image as list
def get_visible_layers(img):
    pdb.gimp_message("Get visible layers")

    gimp.progress_init('Getting visible layers')
    layers = img.layers
    layers_vis = []
    for layer in layers:
        if pdb.gimp_item_get_visible(layer):
            if not pdb.gimp_item_is_group(layer):
                pdb.gimp_layer_add_alpha(layer)
            layers_vis.append(layer)
    gimp.progress_update(1)
    if len(layers_vis) == 0:
        pdb.gimp_message("No visible layer found!")
        gimp.quit()

    pdb.gimp_message("Got visible layers")
    return layers_vis


# Calculates the mean layer of the image
# identically to the original script
def calc_mean(img):
    layers_vis = get_visible_layers(img)
    pdb.gimp_message("mean")

    # Set oppacity of visible layers
    layers_left = len(layers_vis)
    gimp.progress_init('Setting layer opacities')
    for layer in layers_vis:
        layer.opacity = 100.0 / layers_left
        layers_left -= 1
        gimp.progress_update((len(layers_vis) - layers_left) / len(layers_vis))

    gimp.progress_init('Merging layers')
    pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
    gimp.progress_update(1)


# Calculates the average layer with the given average function 'avrg_fnc' of the image
# It just takes the visible layers into account
def calc_avrg(img, avrg_fnc):
    try:
        pdb.gimp_message("Calc average")
        image_x = img.width
        image_y = img.height
        layers_arrays = []
        num_channels = 0
        layers_vis = get_visible_layers(img)

        # get pixel arrays
        # layers_arrays contains the arrays of the layers
        # an array contains the pixel values of one layer as [pixel1_r, pixel1_g, pixel1_b, pixel1_A, pixel2_r, ...]
        gimp.progress_init('Getting pixel values')
        for i,layer in enumerate(layers_vis):
            layer_rgn = layer.get_pixel_rgn(0, 0, image_x, image_y, False, False)
            layers_arrays.append(array("B", layer_rgn[:, :]))
            num_channels = len(layer_rgn[0,0])  # Not pretty in this loop but it works
            gimp.progress_update((i+1) / float(len(layers_vis)))

        # create the merge layer and the destination pixel region
        merged_layer = pdb.gimp_layer_new(img, image_x, image_y, RGB_IMAGE, "merged", 100, NORMAL_MODE)
        pdb.gimp_layer_add_alpha(merged_layer)
        pdb.gimp_image_insert_layer(img, merged_layer, None, 0)
        dest_rgn = merged_layer.get_pixel_rgn(0, 0, image_x, image_y, True, True)
        dest_array = array("B", "\x00" * (image_x * image_y * num_channels))

        pdb.gimp_message("Doing the hard work")
        t = time.time()

        # process the arrays in this manner
        # its faster than actual write out the for loops
        averaged_values = [int(avrg_fnc([arr[i] for arr in layers_arrays])) for i in range(len(layers_arrays[0]))]
        dest_array = array('B',averaged_values)


        pdb.gimp_message(str(time.time() - t))
        pdb.gimp_message("Hard work done!")

        # add dest_array to the dest_rgn
        dest_rgn[:,:] = dest_array.tostring()   # deprecated in Python 3

        # Write out changes
        merged_layer.flush()
        merged_layer.merge_shadow(1)
        merged_layer.update(0, 0, image_x, image_y)
        pdb.gimp_image_merge_visible_layers(img, CLIP_TO_IMAGE)
        pdb.gimp_message("Calced average")

    except:
        # Print the exception details in gimp
        exc_type, exc_obj, exc_tb = sys.exc_info()
        pdb.gimp_message("Type: " +str(exc_type)+"\nLine: " +str(exc_tb.tb_lineno))


def average_layers(img, average):
    try:
        pdb.gimp_image_undo_group_start(img)

        if(average == "mean"):
            calc_mean(img)  # faster than calc_avrg(img, get_mean)

        elif(average == "median"):
            pdb.gimp_message("median")
            calc_avrg(img, get_median)

        elif(average == "mode"):
            pdb.gimp_message("mode")
            calc_avrg(img, get_mode)

        elif(average == "gmode"):
            pdb.gimp_message("gmode")
            pdb.gimp_message("Not implemented yet!")
            #calc_avrg(img, get_gmode)

        elif(average == "range"):
            pdb.gimp_message("range")
            pdb.gimp_message("Not implemented yet!")
            #calc_avrg(img, get_range)

        pdb.gimp_message("finished")
        pdb.gimp_image_undo_group_end(img)
    except:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        pdb.gimp_message("Type: " +str(exc_type)+"\nLine: " +str(exc_tb.tb_lineno))

register(
    'python_fu_average_layers',
    'Merge all layers together using an average value for each pixel',
    'Merge all layers together using an average value for each pixel',
    'Simon Filter',
    'Simon Filter',
    '2019',
    'Average layers ...',
    '*',
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_RADIO, "average", "Set kind of average", "mean",(("Mean (fast)", "mean"), ("Median (slow)", "median"), ("Mode (slow!)", "mode"))),
    ],
    [],
    average_layers, menu="<Image>/Filters/Combine"
)


main()
