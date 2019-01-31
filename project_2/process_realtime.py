"""
ECE196 Face Recognition Project
Author: W Chen

Adapted from:
http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# import numpy as np


#Adapted From Reference #2:
#faces=face_casecade.detectMultiScale(gray, 1.3,5)

# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))

# allow the camera to warmup
time.sleep(0.1)

# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
    """ 
#Adapted From Reference #2:
    cv.rectangle(img, (x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h,x:x+w]
    cv.rectangle(image, roi_gray, )
    """
    
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.resize(geisel.jpg, geisel_2.jpg, Size(), 0.5, 0.5, interpolation)	
    # show the frame
    cv2.imshow("Frame", image)
    # time.sleep(5)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break


#References:
#1. Provided Code for this Assignment
#2. The following webpage: https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
#3. Documentation
