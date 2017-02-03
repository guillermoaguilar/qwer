# -*- coding: utf-8 -*-
"""
Created on Thu Feb  2 16:50:53 2017

@author: guille
"""

from PIL import Image
import numpy as np
import matplotlib.pylab as plt

name = 'grating_8bits'

im = Image.open('examples/%s.png' % name)
plt.imshow(im)
plt.show()

plt.plot(np.array(im)[0,:,0], 'o')
plt.show()


im = Image.open('examples/%s_dither.png' % name)
plt.imshow(im)
plt.show()

plt.plot(np.array(im)[0,:], 'o')
plt.show()

