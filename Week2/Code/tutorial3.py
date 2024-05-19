# Video Display with Quadrant Transformations using OpenCV

import numpy as np
import cv2

# Initialize the camera
cap = cv2.VideoCapture(0)  # 0 is typically the device index for the default camera

while True:
    ret, frame = cap.read()  # Read a frame from the camera
    width = int(cap.get(3))  # Retrieve the width of the camera frame
    height = int(cap.get(4))  # Retrieve the height of the camera frame

    # Create a new image of the same size as the frame, filled with zeros (black)
    image = np.zeros(frame.shape, np.uint8)

    # Resize the captured frame to half its width and height
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    # Place four versions of the smaller frame into the black image:
    # Upper left corner: rotated 180 degrees
    image[:height//2, :width//2] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # Lower left corner: normal orientation
    image[height//2:, :width//2] = smaller_frame
    # Upper right corner: rotated 180 degrees
    image[:height//2, width//2:] = cv2.rotate(smaller_frame, cv2.cv2.ROTATE_180)
    # Lower right corner: normal orientation
    image[height//2:, width//2:] = smaller_frame

    # Display the image in a window named 'frame'
    cv2.imshow('frame', image)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows() 
