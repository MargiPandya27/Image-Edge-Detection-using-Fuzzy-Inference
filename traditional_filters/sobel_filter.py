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

# Apply the Sobel filter
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

# Combine the results to get the edges
sobel_combined = np.sqrt(np.square(sobel_x) + np.square(sobel_y))

# Normalize the result
scaled_sobel = np.uint8(255 * sobel_combined / np.max(sobel_combined))

# Threshold the image to only keep strong edges
threshold = cv2.threshold(scaled_sobel, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Invert the image
inverted = cv2.bitwise_not(threshold)
inverted_image = Image.fromarray(inverted)

# Show the image
inverted_image.save('sobel.png')