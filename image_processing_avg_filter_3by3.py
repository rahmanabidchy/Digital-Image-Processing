# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 11:30:30 2018

@author: lenovo_pc
"""

import numpy as np
import cv2

img = cv2.imread('F:/Abid/CSE428/experimental/man.png', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()

height = img.shape[0]
width = img.shape[1]

#ignoring the edge pixels

for i in np.arange(1, height-1):
    for j in np.arange(1, width-1):
        neighbors = []
        for k in np.arange(-1, 2):
            for l in np.arange(-1, 2):
                a = img.item(i+k, j+l)
                neighbors.append(a)
        c=0
        for m in range(9):
            c = c + neighbors[m]
            
        c= c/9
        img_out.itemset((i,j), c)

cv2.imwrite('F:/Abid/CSE428/experimental/man_avg_3x3.png', img_out)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
