# -*- coding: utf-8 -*-
"""
Created on Fri Nov 30 17:41:25 2018

@author: lenovo_pc
"""

import numpy as np
import cv2

img = cv2.imread('F:/Abid/CSE428/experimental/motijheel-area-dhaka-1960.jpg', cv2.IMREAD_GRAYSCALE)
img_out = img.copy()
img_out1 = img.copy()

height = img.shape[0]
width = img.shape[1]

laplace = (1.0/1.0) * np.array(
        [[ 0, -1, 0],
        [-1, 4, -1],
        [0, -1, 0]])


for i in np.arange(1, height-1):
    for j in np.arange(1, width-1):        
        sum = 0
        for k in np.arange(-1, 2):
            for l in np.arange(-1, 2):
                a = img.item(i+k, j+l)
                w = laplace[1+k, 1+l]
                sum = sum + (w * a)
        b = sum
        c = sum+img.item(i,j)
        img_out.itemset((i,j), b)
        img_out1.itemset((i,j),c)

cv2.imwrite('F:/Abid/CSE428/experimental/motijheel-area-dhaka-1960_3by3_3.jpg', img_out)
cv2.imwrite('F:/Abid/CSE428/experimental/motijheel-area-dhaka-1960_filtered_3by3_3.jpg', img_out1)

cv2.imshow('image',img_out)
cv2.waitKey(0)
cv2.destroyAllWindows()
                
        