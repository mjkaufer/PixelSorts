from PIL import Image
import sys, os
import datetime
import random


# print(parr)
thresh = 5

def val(c, hue):
	if hue:
		return brightness(c);
	return gethue(c);

def brightness(c):
	return (c[0] + c[1] + c[2])/3;

def cont(st,curr, hue):
	return abs(val(st, hue) - val(curr, hue)) <= thresh;

def gethue(col):
	hsv = RGB_2_HSV(col);
	return hsv[0];

def sort(carr,hue, flipbool):#sort the array by brightness
	flip = 1;
	if flipbool:
		flip = posorneg();#if they want alternating, we assign random value
	if hue:
		return sorted(carr, key=lambda el: gethue(el) * flip);#sort by brightness	
	# return sorted(carr, key=lambda el: gethue(el[0]));#sort by brightness
	return sorted(carr, key=lambda el: brightness(el) * flip);#sort by brightness

def posorneg():
	if random.random() > 0.5:
		return -1;
	return 1;

def RGB_2_HSV(RGB):# RGB-HSL code taken from http://stackoverflow.com/a/24153899/2009336
    ''' Converts an integer RGB tuple (value range from 0 to 255) to an HSV tuple '''

    # Unpack the tuple for readability
    R, G, B = RGB

    # Compute the H value by finding the maximum of the RGB values
    RGB_Max = max(RGB)
    RGB_Min = min(RGB)

    # Compute the value
    V = RGB_Max;
    if V == 0:
        H = S = 0
        return (H,S,V)


    # Compute the saturation value
    S = 255 * (RGB_Max - RGB_Min) // V

    if S == 0:
        H = 0
        return (H, S, V)

    # Compute the Hue
    if RGB_Max == R:
        H = 0 + 43*(G - B)//(RGB_Max - RGB_Min)
    elif RGB_Max == G:
        H = 85 + 43*(B - R)//(RGB_Max - RGB_Min)
    else: # RGB_MAX == B
        H = 171 + 43*(R - G)//(RGB_Max - RGB_Min)

    return (H, S, V)

def magic(hue, thresh=50, flip=True):#if hue is true, we sort by hue

	if len(sys.argv) > 1:
		fname = sys.argv[1];
	else:
		fname = "n.jpg"
	img = Image.open(fname);

	parr = img.load()


	for i in range(img.size[0]):	# for every pixel:
		start = 0;
		length = int(random.random() * img.size[1] / 20 + img.size[1] / 10)
		for j in range(img.size[1]):

			# parr[i,j] = (i, j, 100) # set the colour accordingly

			tp = parr[i,j];

			if (not cont(tp, parr[i,start], hue) and abs(start - j) > length) or j + 1 == img.size[1]:#broke the chain or last pixel
				shades = [];
				for e in range(start, j):
					shades.append(parr[i,e]);

				newshades = sort(shades[:], hue, flip);
				for e in range(len(newshades)):
					parr[i,e+start] = newshades[e];

				start = j+1
				length = int(random.random() * img.size[1] / 20 + img.size[1] / 10)

			# parr[i,j] = (0,100,100)

			# if (len(shades) < 100 or cont(parr[i,start], tp)) and len(shades) < 500:#if it's in threshold, add to array
			# 	shades.append( (tp, i, j) );
			# else:#we're done, apply sorted array
			# 	newshades = sort(shades);

			# 	for ind in range(len(shades)):#element is (color, i, j)
			# 		parr[newshades[ind][1],newshades[ind][2]] = newshades[ind][0];#applies new colors

			# 	shades = [];#clear old shades
			# 	start = j;
	img.show()

	detail = "brightness"
	if hue:
		detail = "hue"

	img.save(sys.argv[1] + str(datetime.datetime.now()).replace(":","") + detail + ".jpg", "JPEG");

magic(True);
magic(False);# a lot more smooth

# img = Image.merge(img.mode, parr)
