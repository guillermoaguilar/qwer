# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:50:53 2017

@author: guille
"""

from PIL import Image
import numpy as np
import matplotlib.pylab as plt

im = Image.open('examples/grating_4bits.png')
plt.imshow(im)
plt.show()

plt.plot(np.array(im)[0,:,0])
plt.show()


im = Image.open('examples/grating_4bits_dither.png')
plt.imshow(im)
plt.show()

plt.plot(np.array(im)[0,:,0])
plt.show()

