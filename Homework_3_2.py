from typing import Tuple

import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt


OrginalImage = 0
LightImage = 1
DarkImage = 2

LowContrastImage = 3


ImageArranger = LowContrastImage

HistogramBaseName = "Histogram_Graph"

Operation = ["_Before_Histogram_equ_","_After_Histogram_equ_"]

HomeWorkFileNameBase = "odev3_1_"

FileNames = ["Image_Orginal.png",
             "Image_Light.png",
             "Image_Dark.png",
             "Image_Low_Contrast.png"]


def Save_Image(filename, img):
    directory = path = r'IMAGEPATH
    os.chdir(directory)
    Check = cv2.imwrite(filename, img)
    print("Check = ", Check)


path = r'IMAGEPATH

path = path + FileNames[ImageArranger]

img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
print("Uzantı = ",path)

histg = cv2.calcHist([img],[0],None,[256],[0,256])
HisValueX = np.zeros(256,dtype=int)

Height = img.shape[0]
Width = img.shape[1]

for i in range(Height):
    for j in range(Width):
        HisValueX[img.item(i,j)] += 1



OperationBefore = HistogramBaseName+Operation[0]+FileNames[ImageArranger]
fileOp = OperationBefore

print("file name before operation",fileOp)
plt.plot(histg)
cv2.imshow(FileNames[ImageArranger], img)
plt.savefig(fileOp,dpi=500)
plt.show()




ProbMasFuncArray = np.zeros(256)
sumCheck = 0
for i in range(256):
    ProbMasFuncArray[i] = (HisValueX[i] / (Width* Height))
    sumCheck += ProbMasFuncArray[i]

print(ProbMasFuncArray)
print("Sum check 1 'e eşit olmalı = ",sumCheck)

CumulativeDisFuncArray = np.zeros(256)
for i in range(256):
    for j in range(i+1):
       CumulativeDisFuncArray[i] += ProbMasFuncArray[j]


TFunctionArray = np.zeros(256)

for i in range(256):
    TFunctionArray[i] = round(CumulativeDisFuncArray[i]*255)


print(TFunctionArray)


for i in range(Height):
    for j in range(Width):
        img.itemset(i,j,TFunctionArray[img.item(i,j)])


HistogramEquGrapName = HistogramBaseName+Operation[1]+"_GRAF_"+FileNames[ImageArranger]
histNew = cv2.calcHist([img],[0],None,[256],[0,256])
plt.plot(histNew)
plt.savefig(HistogramEquGrapName,dpi=1000)
plt.show()
OperationAfter = HistogramBaseName+Operation[1]+FileNames[ImageArranger]

print(OperationAfter)
cv2.imshow(FileNames[ImageArranger], img)
Save_Image(OperationAfter,img)
cv2.waitKey(0)
cv2.destroyAllWindows()
