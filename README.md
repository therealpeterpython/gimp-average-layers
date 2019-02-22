## gimp-average-layers

This GIMP plugin merges all layers in an image by taking an average value of each pixel. Useful for noise reduction.

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
2. Select `Filters -> Combine -> Average Layers ...`
3. Choose the average function
4. Wait...


### Problems

The biggest problem is the speed with some of the average functions. 
They work with pixel regions and the hole process is slow for the mean and very slow for the mode function.
If you have an idea to speed things up just let me now or create a merge request.


### Roadmap

I am planing to implement the range average and my own generalized mode average.
If its possible i am speeding the algorith up.


### Changes

The [original function][1] was made created by Oona Räisänen. [John Goodliff][2] added some features like an undo group and progress bar. 
I have restructured everything to implement different kinds of average functions.


### Author & Licensing
Made by Simon Filter (2019, public domain)

[Changes][2] were made by John Goodliff (2018).
[Original function][1] was created by Oona Räisänen (2012-2015, public domain).


[1]: https://github.com/windytan/gimp-average-layers
[2]: https://github.com/jerboa88/gimp-average-layers
