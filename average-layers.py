#!/usr/bin/env python
from gimpfu import *


def average_layers(img, drw, mode):
    gimp.progress_init('Setting layer opacities')
    pdb.gimp_image_undo_group_start(img)
    layers = len(img.layers)
    layers_left = layers

    for layer in img.layers:
        layer.opacity = 100.0 / layers_left
        layers_left -= 1
        gimp.progress_update((layers - layers_left) / layers)

    gimp.progress_init('Flattening image')
    img.flatten()
    gimp.progress_update(1)
    pdb.gimp_image_undo_group_end(img)


register(
    'python_fu_average_layers',
    'Merge all layers together using an average value for each pixel',
    'Merge all layers together using an average value for each pixel',
    'Simon Filter',
    'Simon Filter',
    '2019',
    'Average layers ...',
    'RGB*, GRAY*',
    [
        (PF_IMAGE, "image", "takes current image", None),
        (PF_DRAWABLE, "drawable", "Input layer", None),
        (PF_RADIO, "mode", "Set kind of average", 0,(("Mean", 0), ("Median", 1), ("Mode", 2))),
    ],
    [],
    average_layers, menu="<Image>/Filters/Combine"
)


main()
