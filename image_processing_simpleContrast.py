# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import cv2
import math


path = 'F:/Abid/CSE428/experimental/8uw2T.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)


height = img.shape[0]
width = img.shape[1]

contrast = 1.7

for i in np.arange(height):
    for j in np.arange(width):
        a = img.item(i,j)
        b = math.ceil(a*contrast)
        
        if b > 255:
            b = 255
        img.itemset((i,j),b)
        
cv2.imwrite('F:/Abid/CSE428/experimental/8uw2T_!.jpg',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
