from typing import Tuple

import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt



OperationName = "GammaOperation"
OperationTypes = ["orginalImage","Gamma_2_","Gamma_0_Dot_5"]
path = r'IMAGEPATH'

def Save_Image(filename,img):
    filename = filename+".jpg"
    Check=cv2.imwrite(filename, img)
    print("Check = ",Check)





def R_value(XValue,Bitvalue):
   return (XValue / 255)


pathImage = path = r'IMAGEPATH'

img = cv2.imread(pathImage,cv2.IMREAD_GRAYSCALE)
Operation = OperationName+"_"+OperationTypes[0]
print(Operation)
Height = img.shape[0]
Width = img.shape[1]

Gamma = 0.5
print(Height)
print(Width)
for i in range(Height):
    for j in range(Width):
        r=R_value(img.item(i,j),8)
        NewValue = pow(r,Gamma)
        Adjusted_values = NewValue *255
        img.itemset(i,j,Adjusted_values)
        



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
