# Dynamic Video Drawing: Lines, Rectangles, Circles, and Text using OpenCV

import numpy as np
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 is typically the device index for the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Retrieve the width of the camera frame
    height = int(cap.get(4))  # Retrieve the height of the camera frame

    # Draw a red line from the top-left to the bottom-right corner
    img = cv2.line(frame, (0, 0), (width, height), (255, 0, 0), 10)
    # Draw a green line from the bottom-left to the top-right corner
    img = cv2.line(img, (0, height), (width, 0), (0, 255, 0), 5)
    # Draw a gray rectangle from (100, 100) to (200, 200)
    img = cv2.rectangle(img, (100, 100), (200, 200), (128, 128, 128), 5)
    # Draw a solid blue circle centered at (300, 300) with a radius of 60
    img = cv2.circle(img, (300, 300), 60, (0, 0, 255), -1)
    # Set the font type for text
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Put black text at the bottom-left corner of the screen
    img = cv2.putText(img, 'Tim is Great!', (10, height - 10), font, 2, (0, 0, 0), 5, cv2.LINE_AA)

    # Display the image in a window named 'frame'
    cv2.imshow('frame', img)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows() 
