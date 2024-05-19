# Image Manipulation: Pixel Randomization and Region Copying in OpenCV

import cv2
import random

# Load an image with full color and alpha channel information if present
img = cv2.imread('assets/logo.jpg', -1)  

# Change the first 100 rows to random pixels
for i in range(100):
    for j in range(img.shape[1]):  # Loop through each column in the row
        img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        # Assign random color values for each pixel

# Copy a part of the image from a defined rectangle
tag = img[500:700, 600:900]  # Define the region to copy (rows 500-700, columns 600-900)
img[100:300, 650:950] = tag  # Paste the copied region to a new location (rows 100-300, columns 650-950)

# Display the modified image in a window
cv2.imshow('Image', img)  
cv2.waitKey(0)  # Wait indefinitely until a key is pressed
cv2.destroyAllWindows()  # Close all windows
