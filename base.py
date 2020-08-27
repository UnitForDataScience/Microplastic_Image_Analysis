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

