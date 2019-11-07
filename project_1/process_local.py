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

# Done: Import OpenCV
import cv2

# Done: Edit this function
def process_image(filename):
    img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)
    #cv2.imshow("image",img)
    #cv2.waitKey(0)
    
    img = cv2.resize(img, (img.shape[1]/2, img.shape[0]/2))
    x1 = img.shape[1]/2 - 50
    y1 = img.shape[0]/2 - 50
    x2 = x1 + 100
    y2 = y1 + 100
    cv2.rectangle(img, (x1, y1), (x2, y2), (255,255,255))
    cv2.imwrite("geisel-bw-rectangle.jpg",img)

    return

# Just prints 'Hello World! to screen.
def hello_world():
    print('Hello World!')
    return

# Done: Call process_image function.
def main():
    hello_world()
    process_image("geisel.jpg") 
    new_img = cv2.imread("geisel-bw-rectangle.jpg", cv2.IMREAD_GRAYSCALE)

    cv2.imshow("image",new_img)
    cv2.waitKey(0)
    return


if(__name__ == '__main__'):
    main()
