# -*- coding: utf-8 -*-
"""
Created on Fri Dec  7 20:16:52 2018

@author: lenovo_pc
"""

import numpy as np
import cv2
import math


img = cv2.imread('F:/Abid/CSE428/experimental/woman.jpg', cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]
pixels = width * height

    
hist = np.zeros((256))

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        hist[a] += 1
            
cum_hist = hist.copy()
    
for i in np.arange(1, 256):
    cum_hist[i] = cum_hist[i-1] + cum_hist[i]

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = math.floor(cum_hist[a] * 255.0 / pixels)
        img.itemset((i,j), b)

cv2.imwrite('F:/Abid/CSE428/experimental/woman_equalized.jpg', img)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

