from typing import Tuple

import cv2
import os
import numpy as np
import math

FileNameHighContrast = "HighContrastImage_Operation_"
FileNameLowContrast  = "LowContrastImage_Operation_"
OperationName = ["TH_127","Mean","Median"]

def Save_Image(filename,img):
   directory = path = r'IMAGEPATH'
   os.chdir(directory)
   Check=cv2.imwrite(filename, img)
   print("Check = ",Check)


def Threshold_Function(ImageValue,TH=127, PosSat = 255, NegSat = 0):
   if ImageValue >= TH:
      return PosSat
   else:
      return NegSat


# path
path = r'IMAGEPATH'
# Using cv2.imread() method

img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)

# height, width, number of channels in image
height = img.shape[0] # 
width = img.shape[1] # 


""" Threshold
TH = 127
for i in range(0,img.shape[0]):
 for j in range(0,img.shape[1]):
    th = Threshold_Function(img.item(i,j))
    img.itemset(i,j,th)
imageOperationName = FileNameLowContrast+OperationName[0]+".jpg"
print(imageOperationName)
"""

"""     Mean filter

Sum : int = 0
Average : int = 0
for i in range(0,img.shape[0]):
  for j in range(0,img.shape[1]):
      Sum += img.item(i,j)

Average = Sum /(img.shape[0]*img.shape[1])
print("Ortalama değer =" ,Average)
for i in range(0,img.shape[0]):
  for j in range(0,img.shape[1]):
      CurrentVal = img.item(i,j)
      th = Threshold_Function(CurrentVal,Average,255,0)
      img.itemset(i, j, th)
imageOperationName = FileNameLowContrast+OperationName[1]+"_"+str(Average)+".jpg"
print(imageOperationName)

"""

""" median filter
median = np.median(img)
print("medyan  değeri =" ,median)
for i in range(0,img.shape[0]):
  for j in range(0,img.shape[1]):
      CurrentVal = img.item(i,j)
      th = Threshold_Function(CurrentVal,median,255,0)
      img.itemset(i, j, th)
imageOperationName = FileNameLowContrast+OperationName[2]+"_"+str(median)+".jpg"
print(imageOperationName)
"""



imS = cv2.resize(img, (800,600))
cv2.imshow('image', imS)
Save_Image(imageOperationName,imS)

cv2.waitKey(0)
cv2.destroyAllWindows()