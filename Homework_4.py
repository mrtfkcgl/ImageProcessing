
from PIL import Image
import cv2
import os
import numpy as np
import math
from matplotlib import pyplot as plt
pathImage = path = r'IMAGEPATH'

def Padding_Image(img,paddingValue):
    print("Before padding operation values ",img.shape[0],img.shape[1])
    reflect101 = cv2.copyMakeBorder(img, paddingValue, paddingValue, paddingValue, paddingValue, cv2.BORDER_REFLECT_101)
    #reflect101 = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, None, value=0)
    Height = reflect101.shape[0]  # dikey kolon sayısı
    Width = reflect101.shape[1]  # yatay satır sayısı
    print("Before padding operation values ", reflect101.shape[0], reflect101.shape[1])
    return reflect101

def Save_Image(filename,img):
    filename = filename+".jpg"
    Check=cv2.imwrite(filename, img)
    print("Check = ",Check)

def MeanFilterX_X(img,FilterSize):
    RealCentre = FilterSize-2
    img = Padding_Image(img, RealCentre)
    matrix = np.ones((FilterSize, FilterSize))
    for i in range(RealCentre, img.shape[0] - RealCentre):
        for j in range(RealCentre, img.shape[1] - RealCentre):
            for t in range(0, FilterSize):
                for k in range(0, FilterSize):
                    matrix[t, k] = img.item(i + t - 1, j + k - 1)
            img.itemset(i, j, round(np.sum(matrix) / (FilterSize*FilterSize)))
    return img

def Normalization(Value,Min,Max):
    return round(((Value-Min)/(Max-Min))*255)



def VarianceFilterX_X(img,FilterSize):
    RealCentre = FilterSize - 2
    img = Padding_Image(img, RealCentre)
    VarianceMatrix = np.zeros(((img.shape[0]), (img.shape[0])))
    matrix = np.ones((FilterSize, FilterSize))
    for i in range(RealCentre, img.shape[0] - RealCentre):
        for j in range(RealCentre, img.shape[1] - RealCentre):
            Sum = 0
            Mean = 0
            Variance = 0
            for t in range(0, FilterSize):
                for k in range(0, FilterSize):
                    matrix[t, k] = img.item(i + t - 1, j + k - 1)
                    Sum += matrix[t, k]
            Mean = Sum / np.size(matrix)
            for t in range(0, FilterSize):
                for k in range(0, FilterSize):
                    matrix[t, k] = pow((matrix[t, k]-Mean),2)
                    Variance += (matrix[t, k] / (np.size(matrix)-1))
            Variance = round(Variance)
            VarianceMatrix[i,j] = Variance
    VarianceMax = np.amax(VarianceMatrix)
    VarianceMin = np.amin(VarianceMatrix)
    for i in range(RealCentre, img.shape[0] - RealCentre):
        for j in range(RealCentre, img.shape[1] - RealCentre):
            VarianceMatrix[i, j] = Normalization(VarianceMatrix[i,j],VarianceMin,VarianceMax)
    for i in range(RealCentre, img.shape[0] - RealCentre):
        for j in range(RealCentre, img.shape[1] - RealCentre):
            Value = int(VarianceMatrix[i, j])
            img.itemset(i, j, VarianceMatrix[i, j])
    return img


img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img = MeanFilterX_X(img,15)
#img=VarianceFilterX_X(img,15)
Save_Image("15_15_Filter_Mean_",img)
cv2.imshow('image',img )
cv2.waitKey(0)
cv2.destroyAllWindows()