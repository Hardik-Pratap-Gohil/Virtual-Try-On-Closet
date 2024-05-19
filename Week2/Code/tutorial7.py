# Template Matching to Locate Objects in Images using OpenCV

import numpy as np
import cv2

# Load the main image and convert it to grayscale
img = cv2.resize(cv2.imread('assets/soccer_practice.jpg', 0), (0, 0), fx=0.8, fy=0.8)
# Load the template image (part of the main image to find) and convert it to grayscale
template = cv2.resize(cv2.imread('assets/shoe.PNG', 0), (0, 0), fx=0.8, fy=0.8)
h, w = template.shape  # Get the dimensions of the template image

# List of different methods available for template matching
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
           cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

for method in methods:
    img2 = img.copy()  # Make a copy of the image to draw on

    # Apply the template matching method
    result = cv2.matchTemplate(img2, template, method)
    # Find the minimum and maximum values and their positions
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # If the method is based on minimizing the result, take minimum; otherwise, take maximum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc

    bottom_right = (location[0] + w, location[1] + h)  # Calculate the bottom right corner of the rectangle
    cv2.rectangle(img2, location, bottom_right, 255, 5)  # Draw the rectangle on the image
    
    # Display the result
    cv2.imshow('Match', img2)
    cv2.waitKey(0)  # Wait for a key press to move to the next method
    cv2.destroyAllWindows()  # Close the window displaying the image
