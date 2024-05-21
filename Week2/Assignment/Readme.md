# Assignment: Real-Time Document Scanner

## Objective
Your task is to create a real-time document scanner using Python and OpenCV. This scanner will process video input from a webcam to detect documents in the frame and then transform the perspective to obtain a top-down, scanned image view.

## Requirements
A working webcam  
Python with OpenCV installed

## Assignment Details

### Step 1: Implement Pre-processing Functions

You will need to write a function to convert images to grayscale, apply Gaussian blur, and use edge detection to prepare the image for contour detection.

### Step 3: Contour Detection

Detect contours in the image and identify the one which most likely represents the document (Hint: Use area to find out the biggest contour which is a rectangle)

### Step 4: Perspective Warp

Implement a function to perform a perspective warp that transforms the detected document to a top-down view.

### Step 4: Main Loop

Use a while loop to continuously read from the webcam, process the image, and display the results.

## Submission

Submit your completed Python script via the learning management system. Ensure your script includes comments explaining your code.
