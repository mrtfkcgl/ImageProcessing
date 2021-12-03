from PIL import Image
import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt
path =path = r'IMAGEPATH'
def Save_Image(filename,img):
    filename = filename+".jpg"
    Check=cv2.imwrite(filename, img)
    print("Check = ",Check)

def Normalization(Value,Min,Max):
    return round(((Value-Min)/(Max-Min))*255)

sigmaValues= [100,400]
Kvalues = [5,10,50,100]
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
imgShape = img.shape
Varyans = sigmaValues[1]
Operation = Kvalues[3]

NoiseArray = np.zeros((imgShape[0],imgShape[1]))
HolderArray = np.zeros((imgShape[0], imgShape[1],Operation))
SizeOfNoiseArray = NoiseArray.shape
print(str(Operation)+"_"+str(Varyans))

for k in range(Operation):
    NoiseArray = math.sqrt(Varyans) * np.random.randn(SizeOfNoiseArray[0], SizeOfNoiseArray[1])
    print("k = ",k)
    for i in range(0,imgShape[0]):
        for j in range(0,imgShape[1]):
            HolderArray[i][j][k]=img.item(i,j)+NoiseArray[i][j]
            if HolderArray[i][j][k]> 255:
                HolderArray[i][j][k] = HolderArray[i][j][k] - 128

value = np.zeros(Operation)
MeanArray = np.zeros((imgShape[0],imgShape[1]))
for i in range(0, imgShape[0]):
    for j in range(0, imgShape[1]):
        for k in range(Operation):
            value[k] =  HolderArray[i][j][k]
            MeanArray[i][j]=np.sum(value)/Operation

for i in range(0, imgShape[0]):
    for j in range(0, imgShape[1]):
        img.itemset(i,j,MeanArray[i][j])

cv2.imshow('image',img )
Save_Image(str(Operation)+"_"+str(Varyans),img)
print(str(Operation)+"_"+str(Varyans))
cv2.waitKey(0)
cv2.destroyAllWindows()