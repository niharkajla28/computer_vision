import cv2
import numpy
'''
Syntax: cv2.imread(filename, flag) 

Parameters:

filename: The path to the image file.
flag: The flag specifies the way how the image should be read.
cv2.IMREAD_COLOR – It specifies to load a color image. Any transparency of image will be neglected. 
It is the default flag. Alternatively, we can pass integer value 1 for this flag.
cv2.IMREAD_GRAYSCALE – It specifies to load an image in grayscale mode. Alternatively, 
we can pass integer value 0 for this flag. 
cv2.IMREAD_UNCHANGED – It specifies to load an image as such including alpha channel. 
Alternatively, we can pass integer value -1 for this flag.
Return Value:

The cv2.imread() function return a NumPy array if the image is loaded successfully.
'''
# Activity 1: reading b/w image
# image1 = cv2.imread("flower_bw.png")
# cv2.imshow("Image", image1)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Activity 2: reading color image
# image2 = cv2.imread("color_image.jpeg", 0)
# cv2.imshow("Image", image2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Activity 3: detecting the colors in an image
# image3 = cv2.imread("rgb.png", 1)
# B, G, R = cv2.split(image3)
# cv2.imshow("blue", B)
# cv2.waitKey(0)
# cv2.imshow("green", G)
# cv2.waitKey(0)
# cv2.imshow("red", R)
# cv2.waitKey(0)

# Activity 4: adding, subtracting and weighted addition of two images
# image4 = cv2.imread("galaxy1.jpg")
# image5 = cv2.imread("galaxy2.jpg")
# addition = cv2.add(image4, image5)
# cv2.imshow("Added Images", addition)
# sub = cv2.subtract(image4, image5)
# cv2.imshow("Subtracted Images", sub)
# image6 = cv2.imread("star.jpg")
# image7 = cv2.imread("big_dot.jpg")
# sub2 = cv2.subtract(image6, image7)
# cv2.imshow("Star dot subtraction", sub2)
# # weightedSum = cv2.addWeighted(image4, 1, image5, 1, 0)
# #
# # cv2.imshow("Weighted Image", weightedSum)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# Activity 4: Resizing of image and adding/subtracting
image8 = cv2.imread("person2.png")
image9 = cv2.imread("black.jpg")
height1, width1 = image8.shape[0:2]
print(f"Person--- Height:{height1}, Width:{width1}")
height2, width2 = image9.shape[0:2]
print(f"Background--- Height:{height2}, Width:{width2}")
image10 = cv2.resize(image8, (194, 194))
height3, width3 = image10.shape[0:2]
print(f"Person resized--- Height:{height3}, Width:{width3}")
image11 = cv2.resize(image9, (194, 194))
cv2.imshow("black background", image11)
person_bg = cv2.add(image10, image11)
# person_bg = cv2.addWeighted(image10, 0.3, image11, 1, 0)
cv2.imshow("Addition of person", person_bg)
cv2.waitKey(0)