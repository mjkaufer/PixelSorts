# PixelSorts

## Usage

To use, enter the following into your terminal

`python main.py [file name]`

After a bit (the calculations are expensive and Python is slow), two images should be displayed and saved. One should have `hue` in the filename while the other should have `brightness`. This is how the images were sorted.

## How Does It Work?

Basically, the program grabs a pixel. It then goes down this pixel's column until the length of pixels it has traversed has exceeded a certain number, or until the pixel being traversed is of a significant distance from the original pixel's hue or brightness. Then, all pixels in this line of pixels traversed are sorted based on hue or brightness. The sort fluctuates between ascending and descending to give the image more variety. This is a pretty simple implementation of pixel sorting. There are more elaborate and cooler things that can be done. Fork this and make something cooler!
