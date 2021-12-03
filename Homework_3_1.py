from typing import Tuple

import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt
path = r'IMAGEPATH'


def Save_Image(filename,img):
    filename = filename+".jpg"
    Check=cv2.imwrite(filename, img)
    print("Check = ",Check)



path = r'IMAGEPATH'
img = cv2.imread(ImagePath,cv2.IMREAD_GRAYSCALE)
# height, width, number of channels in image
height = img.shape[0] # dikey kolon
width = img.shape[1] # yatay satır

OperationName = "_7_Bit_Value=128"
maskValue = 128


print("mask = ",maskValue)
for i in range(height):
    for j in range(width):
        value = img.item(i,j) & maskValue
        print(value)
        img.itemset(i,j,value)

cv2.imshow('image', img)
cv2.waitKey(0)
OperationName = OperationName +".jpg"
Save_Image(OperationName,img)
cv2.destroyAllWindows()
