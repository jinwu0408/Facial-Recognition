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
	a=grayscale_image.size()
	print(a)
	cv2.resize(src=grayscale_image, dst='Geisel__3.jpg', dsize=a,fx=0.5, fy=0.5)#Step 3	
	cv2.rectangle('Geisel__3.jpg', cv2.GetSize()/2-(50,50), cv2.GetSize()+(50,50), (256,256,256))
	cv2.imwrite('geisel-bw-rectangle.png','Geisel__3.jpg')
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
