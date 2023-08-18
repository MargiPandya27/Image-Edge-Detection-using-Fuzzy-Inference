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
image = cv2.imread("Images\Input_Image.jpeg")  

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Define the Prewitt kernels
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]], dtype=np.float32)
kernel_y = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]], dtype=np.float32)

# Apply the Prewitt filter
prewitt_x = cv2.filter2D(gray, cv2.CV_64F, kernel_x)
prewitt_y = cv2.filter2D(gray, cv2.CV_64F, kernel_y)

# Combine the results to get the edges
prewitt_combined = np.sqrt(np.square(prewitt_x) + np.square(prewitt_y))

# Normalize the result
scaled_prewitt = np.uint8(255 * prewitt_combined / np.max(prewitt_combined))

# Threshold the image to only keep strong edges
threshold = cv2.threshold(scaled_prewitt, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

# Invert the image
inverted = cv2.bitwise_not(threshold)
inverted_image = Image.fromarray(inverted)

# Show the image
inverted_image.save('prewitts.png')