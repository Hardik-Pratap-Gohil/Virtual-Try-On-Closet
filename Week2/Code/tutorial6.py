# Corner Detection and Visualization in a Chessboard Image using OpenCV

import numpy as np
import cv2

# Load an image of a chessboard
img = cv2.imread('assets/chessboard.png')
# Resize the image to 75% of its original size for better handling
img = cv2.resize(img, (0, 0), fx=0.75, fy=0.75)
# Convert the image to grayscale for feature detection
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detect strong corners on the chessboard image
corners = cv2.goodFeaturesToTrack(gray, 100, 0.01, 10)
# Convert corner coordinates to integer values (necessary for drawing functions)
corners = np.int0(corners)

# Draw red circles at each detected corner
for corner in corners:
    x, y = corner.ravel()  # Flatten the corner array to x, y coordinates
    cv2.circle(img, (x, y), 5, (255, 0, 0), -1)  # Draw circle with radius 5

# Draw lines connecting each pair of corners
for i in range(len(corners)):
    for j in range(i + 1, len(corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size=3)))  # Random color for each line
        cv2.line(img, corner1, corner2, color, 1)

# Display the result
cv2.imshow('Frame', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
