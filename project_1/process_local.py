import cv2

def process_image():
	grayscale_image=cv2.imread('geisel.jpg', flags=0)#Task 1 and Task 2
	image_3=cv2.resize(src=grayscale_image, dsize=(0,0), fx=0.5, fy=0.5)#Task 3	
	image_4=cv2.rectangle(image_3, (image_3.shape[1]/2-50,image_3.shape[0]/2+50),(image_3.shape[1]/2+50,image_3.shape[0]/2-50),  (256,256,256),3)#Task 4
	cv2.imwrite('geisel-bw-rectangle.jpg',image_4)#Task 5
	return


def hello_world():
    print('Hello World!')#"Hello World!", without the quotation marks, gets printed to the standard output, which can be a computer screen.
    return

def main():
	hello_world()
	process_image()#The "process_image" function gets called.
	return


if(__name__ == '__main__'):
    main()



"""
References:
1. Certain Subpages of the Following Website: https://docs.opencv.org/
2. Relavant Resources Given to Students who had to Complete Project 1 of the Face Recognition Projects for the University of California, San Diego's ECE 196 course in Winter 2019
	Reference 2 includes the following resources:
	i. At Least One Piazza Post for the University of California, San Diego's ECE 196 in Winter 2019
	ii. Project 1 of the Face Recongnition Projects for the University of California, San Diego's ECE 196 course in Winter 2019
 
"""
