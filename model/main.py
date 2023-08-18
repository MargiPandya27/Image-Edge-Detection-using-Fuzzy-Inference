import cv2
import numpy as np
from scipy.signal import convolve2d
from skimage.io import imread, imshow
import math
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


image = cv2.imread("Input_Image.jpeg")  
gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

G1 = np.array([[1,1],[-1,-1]])
G2 = G1.transpose()

Ix = convolve2d(gray_image, G1)

Iy = convolve2d(gray_image, np.transpose(G1))


def G(x, mean, std):
  return np.exp(-0.5*np.square((x-mean)/std))


ux=G(Ix,0,50)

uy=G(Iy,0,18)



rows,cols=ux.shape

def inference(gray_image, ux, uy):
    Iinf=np.zeros(list(gray_image.shape),dtype='float')
    for i in range(ux.shape[0]):
        for j in range(ux.shape[1]):
            if(ux[i][j]>=0.8 and uy[i][j]>=0.8):
                Iinf[i][j]= min(ux[i][j],uy[i][j])

    return Iinf

def defuzzification(gray_image, ux, uy):
    rows,cols=ux.shape
    Idef=np.empty(list(gray_image.shape),dtype='float')
    for i in range(rows):
        for j in range(cols):
            if(ux[i][j]>=0.8 and uy[i][j]>=0.8):
                Idef[i][j]= 255

    return Idef
      

#for i in range(rows-1):
#  for j in range(cols-1):
#    if(Iout[i][j]>0.8):
#      Iout[i][j]= 0
#
#    else:
#      Iout[i][j] =255

# Given NumPy array
arr = np.array([[255, 0, 0], [0, 255, 0], [0, 0, 255]])

# Convert the array to a PIL Image
Iinf = inference(gray_image, ux, uy)
Iout = defuzzification(gray_image, ux, uy)
img = Image.fromarray(Iout.astype('uint8'))

# Save the image as a PNG file
img.save('my_image.png')
