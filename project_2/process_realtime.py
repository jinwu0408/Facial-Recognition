"""
ECE196 Face Recognition Project

Adapted from:
1. http://www.pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
2. W Chen's Code for the ECE196 Face Recognition Project
3. https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html

Use this code as a template to process images in real time, using the same techniques as the last challenge.
You need to display a gray scale video with 320x240 dimensions, with box at the center
"""


# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
# import numpy as np

face_cascade = cv2.CascadeClassifier('/usr/local/share/opencv4/haarcascades/haarcascade_frontalface_default.xml')

#Adapted From Reference #2:
#faces=face_casecade.detectMultiScale(gray, 1.3,5)


# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
camera.resolution = (320, 240)
camera.framerate = 32
rawCapture = PiRGBArray(camera, size=(320, 240))
pose = 0
"""
x=(120-100)/2
y=(160-100)/2
w=100
h=100
"""
# allow the camera to warmup
time.sleep(0.1)
counter=0;
found_face=False
# capture frames from the camera
for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
    # grab the raw NumPy array representing the image, then initialize the timestamp
    # and occupied/unoccupied text
    image = frame.array
     
    #Adapted From Reference #2:
    
    image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    faces=face_cascade.detectMultiScale(image, 1.3,5)
    #for(x,y,w,h) in faces:
    for(x,y,w,h) in faces:
        maxWH = max([w,h])
        #image2 = cv2.rectangle(image, (x,y),(x+maxWH,y+maxWH),(255,255,255),2)
        found_face=True

        # Crop to rectangle (x,y) -> (x+maxWH, y+maxWH)
        croppedIm = image[y:y+maxWH, x:x+maxWH]
        resizeIm = cv2.resize(croppedIm, (244,244))
        cv2.imshow("Cropped", croppedIm)
        cv2.imshow("resized",resizeIm)
        if (counter >9) :
            counter = 0
            pose = input("Please enter the Pose number")
        cv2.imwrite("./Images_Akhil/Pose%sFrame%s.PNG" % (pose,counter), resizeIm)
        counter=counter+1
    # show the frame
    cv2.imshow("Frame", image)
    # time.sleep(5)
    key = cv2.waitKey(1) & 0xFF

    # clear the stream in preparation for the next frame
    rawCapture.truncate(0)

    # if the `q` key was pressed, break from the loop
    if key == ord("q"):
        break
    found_face=False
    
            #break

#References:
#1. Provided Code for this Assignment
#2. The following webpage: https://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
#3. Documentation on OpenCV. Python, etc.
#4. https:/projects.raspberrypi.org/en/projects/getting-started-with-picamera6
