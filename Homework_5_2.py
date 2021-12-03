from PIL import Image
import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt
pathOrginal = path = r'IMAGEPATH'
pathNoise = path = r'IMAGEPATH'
FileName ="100_400"


def WriteFile(Filename,MAE,MSE,PSNR):
    StringPSNR = str(PSNR)
    StringMAE  = str(MAE)
    StringMSE = str(MSE)
    print(Filename)
    print("MAE value: " + StringMAE)
    print("PSNR value: "+StringPSNR)
    print("MSE value: " + StringMSE)
    f = open(Filename+".txt","w",encoding='utf-8')
    f.write(Filename+'\n')
    f.write("MAE value: "+StringMAE+'\n')
    f.write("MSE value:"+StringMSE+'\n')
    f.write("PSNR value: "+StringPSNR+'\n')
    f.close()

def Save_Image(filename,img):
    filename = filename+".jpg"
    Check=cv2.imwrite(filename, img)
    print("Check = ",Check)


imgNoise = cv2.imread(pathNoise, cv2.IMREAD_GRAYSCALE)
img = cv2.imread(pathOrginal, cv2.IMREAD_GRAYSCALE)
imgSize = img.shape
ErrorMatrix = np.zeros((imgSize[0],imgSize[1]))
MSE = 0
MAE = 0
PSNR = 0
Psignal = pow(255,2)
Size= imgSize[1]*imgSize[0]
Value = 0
for i in range(imgSize[0]):
    for j in range(imgSize[1]):
        ErrorMatrix[i][j] = img.item(i,j)-imgNoise.item(i,j)
        Value = ErrorMatrix[i][j]
        MSE += pow(Value,2)
        MAE += abs(Value)



MSE = MSE/Size
MAE = MAE/Size
PSNR = 20*math.log10(Psignal/math.sqrt(MSE))

cv2.imshow('imageNoise',imgNoise)
cv2.imshow('imageOrgin',img)

WriteFile(FileName,MAE,MSE,PSNR)
cv2.waitKey(0)
cv2.destroyAllWindows()
