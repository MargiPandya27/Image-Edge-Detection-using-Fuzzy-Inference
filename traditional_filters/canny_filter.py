import cv2
import numpy as np
import cv2
import numpy as np
from scipy.signal import convolve2d
from skimage.io import imread, imshow
import math
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image

# Load the image
image = cv2.imread("Input_Image.jpeg")  

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Canny edge detector
edges = cv2.Canny(gray, 100, 200)

# Invert the image
inverted = cv2.bitwise_not(edges)
inverted_image = Image.fromarray(inverted)

# Show the image
inverted_image.save('canny.png')