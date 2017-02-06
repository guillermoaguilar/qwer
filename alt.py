# -*- coding: utf-8 -*-
"""
another try


@author: G. Aguilar, Feb 2017
"""

import time
from datetime import timedelta
import numpy as np
from PIL import Image

starttime = time.time()


fname = 'examples/grating_8bits.png'

img = Image.open(fname).convert('L')

nsteps = 2**4

v = np.arange(0, 2**8) # source palette, 256 steps
m = np.linspace(0, 2**8-1, 2**4)  # destinaton palette, 16 steps
w = m.repeat(2**4)
w = np.round(w).astype('int')


#threshold = 128*[0] + 128*[255] # 2**1
# mapping
threshold = dict(zip(list(v),list(w)))


## Floyd-Steinberg algorithm
#"""
#https://en.wikipedia.org/wiki/Floyd–Steinberg_dithering
#
#Pseudocode:
#
#for each y from top to bottom
#   for each x from left to right
#      oldpixel  := pixel[x][y]
#      newpixel  := find_closest_palette_color(oldpixel)
#      pixel[x][y]  := newpixel
#      quant_error  := oldpixel - newpixel
#      pixel[x+1][y  ] := pixel[x+1][y  ] + quant_error * 7/16
#      pixel[x-1][y+1] := pixel[x-1][y+1] + quant_error * 3/16
#      pixel[x  ][y+1] := pixel[x  ][y+1] + quant_error * 5/16
#      pixel[x+1][y+1] := pixel[x+1][y+1] + quant_error * 1/16
#
#find_closest_palette_color(oldpixel) = floor(oldpixel / 256)
#"""

im = np.array(img)

for y in range(im.shape[1]):
    for x in range(im.shape[0]):
        old = im[x, y]
        new = threshold[old]
        im[x, y] = new
        
        err = (old - new) # difference from right value

        nxy = (x+1, y)
        try:
            im[nxy] = im[nxy] + err*7.0/16.0
        except IndexError:
            pass

        nxy = (x-1, y+1)
        try:
            im[nxy] = im[nxy] + err*3.0/16.0
        except IndexError:
            pass

        nxy = (x, y+1)
        try:
            im[nxy] = im[nxy] + err*5.0/16.0
        except IndexError:
            pass

        nxy = (x+1, y+1)
        try:
            im[nxy] = im[nxy] + err*1.0/16.0
        except IndexError:
            pass


## saves
name= fname.split(".")[0]+'_dither.png'
img= Image.fromarray(im)
img.convert('L').save(name)


print "time elapsed: %s" % str(timedelta(seconds=time.time()-starttime))
