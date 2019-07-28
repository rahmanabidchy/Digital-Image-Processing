# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:30:30 2018

@author: lenovo_pc
"""

import numpy as np
import cv2

img = cv2.imread('F:/Abid/CSE428/experimental/plane_noisy.png', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

#ignoring the edge pixels

for i in np.arange(2, height-2):
    for j in np.arange(2, width-2):
        neighbors = []
        for k in np.arange(-2, 3):
            for l in np.arange(-2, 3):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        neighbors.sort()
        median = neighbors[12]
        b = median
        img_out.itemset((i,j), b)

cv2.imwrite('F:/Abid/CSE428/experimental/plane_noisy_5x5.png', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
