# Real-Time Blue Color Detection and Display using OpenCV

import numpy as np
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 is typically the device index for the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Retrieve the width of the camera frame
    height = int(cap.get(4))  # Retrieve the height of the camera frame

    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # Define the range of blue color in HSV
    lower_blue = np.array([90, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # Create a mask that captures areas of the frame that are blue
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Apply the mask to the frame, keeping only the blue parts
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame and the mask
    cv2.imshow('frame', result)  # Show the result of the mask applied
    cv2.imshow('mask', mask)  # Show the binary mask

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows() 
