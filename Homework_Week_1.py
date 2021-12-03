import cv2
import numpy as np
import math



def Quant_Function(K_Bit,Value_Max = 256,Value_Min = 0):
    return (Value_Max - Value_Min) / (2**K_Bit)

def Dac_Funciton(Current_Val,K_Bit,Value_Max = 256,Value_Min = 0):
    Quant =Quant_Function(K_Bit,Value_Max,Value_Min)
    return Quant*(Current_Val+(1/2))
"""
Test case Dac_Function
for i in range(2):
    print(Dac_Funciton(i,1))
"""
def Adc_Funciton(Current_Val,K_Bit,Value_Max = 256,Value_Min = 0):
    Quant =Quant_Function(K_Bit,Value_Max,Value_Min)
    Ofsett = Current_Val - Value_Min
    Adc_Value = (Ofsett / Quant)
    return math.floor(Adc_Value)
"""
# test case for Adc_Function() 

for i in range(259):
    if i == 127:
        print("127---- ", Adc_Funciton(i, 1))
    elif i == 128:
        print("128---- ", Adc_Funciton(i, 1))
    else:
        print("i --",i,Adc_Funciton(i, 1))
"""

# path
path = r'IMAGEPATH'
img = cv2.imread(path,cv2.IMREAD_GRAYSCALE)
cv2.imshow('8 Bit Image', img)
cv2.waitKey(0)



# Get image shape
Height = img.shape[0]
Width = img.shape[1]


K_Bit = 1 #Constant changed according to the desired Bit value 7,6,5,4,3,2,1


BaseCaption = str(K_Bit)
BaseCaption += "- Bit Image"

for i in range(Height):
    for j in range(Width):
        AdcValue = Adc_Funciton(img.item(i,j),K_Bit)
        NewValue = Dac_Funciton(AdcValue,K_Bit)
        print("Old value = " ,AdcValue,"  New Value = ",NewValue)
        img.itemset(i,j,NewValue)


cv2.imshow(BaseCaption,img)
cv2.waitKey(0)

cv2.destroyAllWindows()