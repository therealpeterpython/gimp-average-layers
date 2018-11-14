#!/usr/bin/env python
from gimpfu import *


def average_layers(img, drw):
	gimp.progress_init('Setting layer opacities')
	pdb.gimp_undo_push_group_start(img)
	layers = len(img.layers)
	layers_left = layers

	for layer in img.layers:
		layer.opacity = 100.0 / layers_left
		layers_left -= 1
		gimp.progress_update((layers - layers_left) / layers)

	gimp.progress_init('Flattening image')
	img.flatten()
	gimp.progress_update(1)
	pdb.gimp_undo_push_group_end(img)


register(
	'python_fu_average_layers',
	'Merge all layers together using the average value for each pixel',
	'Merge all layers together using the average value for each pixel',
	'John Goodliff',
	'John Goodliff',
	'2018',
	'<Image>/Image/Average Layers',
	'RGB*, GRAY*',
	[],
	[],
	average_layers
)


main()
