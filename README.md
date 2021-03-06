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

The biggest problem is the speed. The mean average works different from the others and is thereby really fast.
If you choose one of the other average functions you maybe have to wait a long time. 
The plugin works with pixel regions and the hole process is slow for the mean and very slow for the mode function.

Another issue is the fact that you can not cancel the execution properly.

The script works on every channel and takes it values from there independetly. It would be better to work
with the hole pixel to avoid creating new color combinations.

If you have a solution to this problems just let me now.


### Roadmap

I am planing to implement the range average and my own generalized mode average.  
If it is possible i will speeding the algorithm up.  
Just use the selection, not the whole image.  

### Changes

The [original function][1] was made created by Oona Räisänen. [John Goodliff][2] added some features like an undo group and progress bar.  
I have restructured everything to implement different kinds of average functions.


### Author & Licensing

Made by Simon Filter (2019, public domain)

[Changes][2] were made by John Goodliff (2018).  
[Original function][1] was created by Oona Räisänen (2012-2015, public domain).


[1]: https://github.com/windytan/gimp-average-layers
[2]: https://github.com/jerboa88/gimp-average-layers
