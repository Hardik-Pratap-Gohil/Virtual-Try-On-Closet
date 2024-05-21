# Assignment: Real-Time Document Scanner

## Objective
Your task is to create a real-time document scanner using Python and OpenCV. This scanner will process video input from a webcam to detect documents in the frame and then transform the perspective to obtain a top-down, scanned image view.

## Requirements
A working webcam  
Python with OpenCV installed

## Assignment Details

### Step 1: Implement Pre-processing Functions

You will need to write a function to convert images to grayscale, apply Gaussian blur, and use edge detection to prepare the image for contour detection.

### Step 2: Contour Detection

Detect contours in the image and identify the one which most likely represents the document (Hint: Use area to find out the biggest contour which is a rectangle)

### Step 3: Perspective Warp

Implement a function to perform a perspective warp that transforms the detected document to a top-down view.

### Step 4: Main Loop

Use a while loop to continuously read from the webcam, process the image, and display the results.

## Submission

Submit your completed Python script along with screenshot of a document(or any rectangular object it detected) via the google form. Ensure your script includes comments explaining your code.

## Challenges

You can face a number of challenges while doing the assignment:
1) You need to make a bounding box for the document detected. So for that you need to give the points to the respective function in a certain order and the points you detected from Step 2 will not always be in that order. So you need to reorder the points before trying to make a perspective warp
2) Many a times, lighting has a serious effect. So make sure you try to detect documents in good lighting conditions and in a contrasting background
3) Sometimes, there is fluttering of the image detected, so you can break the while loop in Step 4 as soon as you detect a document
