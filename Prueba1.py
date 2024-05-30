import numpy as np
import cv2
import pydicom as dicom
from skimage import exposure
from matplotlib import pyplot as plt
from math import log, exp

ds=dicom.dcmread('/home/maria/Documentos/dicomVisualizer/dicomsBuenosBreastDensity/f66d8acdabdb94824a4075e524eed08e/3ed8651c06be656824ba801feffb41e9_R_ML.dcm')
dcm_sample=ds.pixel_array

##########################NEGATIVO############################

maximo = np.max(dcm_sample)
lut = np.zeros(maximo+1)
for i in range(maximo+1):
    lut[i] = maximo - i
print(lut)
# negativo = cv2.LUT(dcm_sample,salida)
negativo = lut[dcm_sample]
print(negativo)

img = (negativo/maximo*255).astype(np.uint8)
img1 = (dcm_sample/maximo*255).astype(np.uint8)
img_R = cv2.resize(img, (960, 1024)) 
img1_R = cv2.resize(img1, (960, 1024))
cv2.imshow('positivo',img1_R)
cv2.imshow('negativo',img_R)
cv2.waitKey(0)

##########################FUNCIÓN POTENCIA############################

minimo = np.min(dcm_sample)
lut = np.zeros(maximo+1)
gamma = 3
for i in range(maximo+1):
    lut[i] = maximo*(((i-minimo)/(maximo-minimo))**gamma)
print(lut)
potencia = lut[dcm_sample]
print(potencia)

img = (potencia/maximo*255).astype(np.uint8)
img_R = cv2.resize(img, (960, 1024)) 
cv2.imshow('original',img1_R)
cv2.imshow('potencia',img_R)
cv2.waitKey(0)

##########################FUNCIÓN LOGARÍTMICA############################

lut = np.zeros(maximo+1)
for i in range(maximo+1):
    lut[i] = maximo*log(1+((i-minimo)/(maximo-minimo)))
    # lut[i] = (exp(i / maximo) - 1) * (maximo - minimo) + minimo
print(lut)

logaritmo = lut[dcm_sample]
print(logaritmo)

img = (logaritmo/maximo*255).astype(np.uint8)
img_R = cv2.resize(img, (960, 1024)) 
cv2.imshow('original',img1_R)
cv2.imshow('logaritmo',img_R)
cv2.waitKey(0)




