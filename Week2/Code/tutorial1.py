# Image Loading, Resizing, Rotating, and Saving


import cv2

# Load an image from file
img = cv2.imread('assets/logo.jpg', 1)  
# The '1' indicates to load the image in color. If you use 0, it will be in grayscale.

# Resize the image to half of its original size
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)  
# (0, 0) tells OpenCV to ignore the manual size; fx and fy tell it to scale the width and height by 0.5 respectively.

# Rotate the image 90 degrees clockwise
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)  
# Uses a predefined function in OpenCV to rotate the image.

# Save the modified image to a new file
cv2.imwrite('new_img.jpg', img)  
# Writes the modified image to a file in JPEG format at the specified path.

# Display the modified image in a window
cv2.imshow('Image', img)  
# The first parameter is the window name, and the second is the image to display.

# Wait for a key press indefinitely
cv2.waitKey(0)  
# The parameter 0 means it will wait indefinitely for a user's key press.

# Close all OpenCV windows
cv2.destroyAllWindows()  
# This function destroys all of the opened HighGUI windows.
