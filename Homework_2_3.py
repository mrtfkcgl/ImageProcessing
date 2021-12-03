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


def linner_Func(Value):
    if (Value > 190)and(Value<192):
        a=0.85
        c=35
        return (Value*a+c)
    elif(Value >= 192)and (Value<195):
        a=0.65
        c=25
        return (Value*a+c)
    elif(Value>=195)and (Value <= 200):
        a=0.55
        c=12
        return (Value*a+c)
    elif(Value>=200) and (Value<=202):
        a=0.45
        c=1
        return (Value*a+c)
    elif(Value>202) and (Value<=205):
        a = 0.35
        c= 22
        return (Value*a+c)
    else:
        a=1
        c=45
        return (Value*a+c) 


def R_value(XValue,Bitvalue):
   return (XValue / 255)


pathImage = path = r'IMAGEPATH'

img = cv2.imread(pathImage,cv2.IMREAD_GRAYSCALE)
Operation = "Bonus_Image_"
print(Operation)
Height = img.shape[0]
Width = img.shape[1]

print(Height)
print(Width)
for i in range(Height):
    for j in range(Width):
        bonus=linner_Func(img.item(i,j))
        img.itemset(i,j,bonus)
        



histg = cv2.calcHist([img],[0],None,[256],[0,256]) 
plt.plot(histg)
fileOp = Operation+".png"
plt.savefig(fileOp,dpi=1000)
plt.show()
imS = cv2.resize(img, (800,600))
cv2.imshow('image', imS)
Save_Image(Operation,imS)
cv2.waitKey(0)
cv2.destroyAllWindows()
