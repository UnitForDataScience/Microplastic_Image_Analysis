# -------------------------------------------------------------------------------
# Name: classify.py
# Purpose: Base code to begin working with Microplastics data
#
# Author(s):    David Little
#
# Created:      09/01/2020
# Updated:
# Update Comment(s):
#
# TO DO:
#
# -------------------------------------------------------------------------------
import os

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from skimage.io import imread

from tensorflow.keras import layers
from tensorflow.keras import Model
from tensorflow.keras.optimizers import RMSprop
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing.image import img_to_array, load_img


# Assigning directories
norm_train_dir = 'chest_xray/train/NORMAL'
pne_train_dir = 'chest_xray/train/PNEUMONIA'

norm_test_dir = 'chest_xray/test/NORMAL'
pne_test_dir = 'chest_xray/test/PNEUMONIA'

# generating lists of filenames
norm_train_files = os.listdir(norm_train_dir )
pne_train_files = os.listdir(pne_train_dir )
norm_test_files = os.listdir(norm_test_dir )
pne_test_files = os.listdir(pne_test_dir )

# User output validation (NOTE: file names should all be different)
print(norm_train_files[:5])
print(pne_train_files[:5])
print(norm_test_files[:5])
print(pne_test_files[:5])