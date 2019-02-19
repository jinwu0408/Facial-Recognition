"""
ECE196 Face Recognition Project
Author: Will Chen

Prerequisite: You need to install OpenCV before running this code
The code here is an example of what you can write to print out 'Hello World!'
Now modify this code to process a local image and do the following:
1. Read geisel.jpg
2. Convert color to gray scale
3. Resize to half of its original dimensions
4. Draw a box at the center the image with size 100x100
5. Save image with the name, "geisel-bw-rectangle.jpg" to the local directory
All the above steps should be in one function called process_image()
"""

# TODO: Import OpenCV
import cv2
# TODO: Edit this function
def process_image():
	grayscale_image=cv2.imread('geisel.jpg', flags=0)#Step 1 and Step 2
	cv2.imwrite('Geisel__1_2.jpg', grayscale_image)
	image_3=cv2.resize(src=grayscale_image, dsize=(0,0), fx=0.5, fy=0.5)#Step 3	
	#print(image_3)
#	cv2.imshow('Window', image_3)
	cv2.imwrite('Geisel__3.jpg', image_3)
	#image_3=cv2.imread('Geisel__3.jpg')	
#	image_4=cv2.rectangle(image_3, image_3.shape(:2)/2-(50,50), image_3.shape(:2)+(50,50), (256,256,256))#Step 4
	image_4=cv2.rectangle(image_3, (image_3.shape[0]/2-50,image_3.shape[1]/2-50), (image_3.shape[0]/2+50,image_3.shape[1]/2+50), (256,256,256))#Step 4
 
	#image_3=cv2.imread('Geisel__3.jpg')	
	cv2.imwrite('geisel-bw-rectangle.png',image_4)#Step 5
	return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# TODO: Call process_image function.
def main():
	hello_world()
	process_image()
	return


if(__name__ == '__main__'):
    main()

#References
# 1. Certain Subpages of the Following Website: https://docs.opencv.org/
# 2. Piazza Posts for UCSD's ECE 196 in Winter 2019
