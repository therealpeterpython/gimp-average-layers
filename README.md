## gimp-average-layers

This GIMP plugin merges all layers in an image by taking the average value of each pixel. Useful for noise reduction.

![Example](/example.png?raw=true "Example")


### Installing

#### Windows

1. Move this plugin into the `%appdata%/GIMP/2.8/plug-ins/` directory.
2. Restart GIMP.


#### Linux

1. Move this plugin into the `~/.gimp-2.8/plug-ins/` directory.
2. `chmod +x ~/.gimp-2.8/plug-ins/average-layers.py`
3. Restart GIMP.


#### Mac OS X

1. Move this plugin into the `~/Library/Application\ Support/GIMP/2.8/plug-ins/` directory.
2. `chmod +x ~/Library/Application\ Support/GIMP/2.8/plug-ins/average-layers.py`
3. Restart GIMP.


### Usage

1. Select `File -> Open as Layers...` to open the images you wish to blend.
2. Select `Image -> Average Layers`

### Changes

The [original function][1] was made created by Oona Räisänen. I have added some small features to make it more usable in production like an undo group and progress bar.


### Author & Licensing
Made by John Goodliff (2018). All rights reserved.

[Original function][1] was created by Oona Räisänen (2012-2015, public domain).


[1]: https://github.com/windytan/gimp-average-layers
