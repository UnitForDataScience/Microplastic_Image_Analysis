# -------------------------------------------------------------------------------
# Name: base.py
# Purpose: Base code to begin working with Microplastics data
#
# Author(s):    David Little
#
# Created:      07/13/2020
# Updated:
# Update Comment(s):
#
# TO DO:
#
# -------------------------------------------------------------------------------

#import tensorflow


import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.io import imread

from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array, load_img

import numpy as np
import cv2
import cv2 as cv
from matplotlib import pyplot as plt


mp_1 = cv2.imread("MP_pics/isolate/type_3_uniform/PP 9d001-MERGE-0.jpeg") #import image
#mp_1_CO = cv2.cvtColor(mp_1, cv2.COLOR_BGR2RGB) # Color conversion
mp_1_BW = cv2.cvtColor(mp_1, cv2.COLOR_BGR2GRAY) #change to grayscale

#plt.imshow(mp_1_CO)
plt.imshow(mp_1_BW,'gray') #this is matplotlib solution (Figure 1)
plt.xticks([]), plt.yticks([])
plt.show()

cv2.imshow('mp_1_BW', mp_1_BW) #this is for native openCV display


#mp_1_BW_blur = cv2.GaussianBlur(mp_1_BW,(5,5),0)
mp_1_BW_blur = cv.bilateralFilter(mp_1_BW,9,75,75)
cv2.imshow('mp_1_BW_blur', mp_1_BW_blur)

ret,thresh = cv2.threshold(mp_1_BW_blur,0,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
cv2.imshow('mp_1_BW_blur_th', thresh)

kernel = np.ones((5,5),np.uint8) #square image kernel used for erosion
erosion = cv2.erode(thresh, kernel,iterations = 1) #refines all edges in the binary image

opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel) #this is for further removing small noises and holes in the image
cv2.imshow('closing', closing)

contours, hierarchy = cv2.findContours(closing,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE) #find contours with simple approximation

cv2.imshow('cleaner', closing) #Figure 3
cv2.drawContours(closing, contours, -1, (255, 255, 255), 4)


#___________________________________________ TEST CODE BELOW _________________________________________

