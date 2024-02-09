#STEP 1: From color image to gray scale image

# import cv2
#
# img = cv2.imread('girl.jpeg')
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RBG, BGR
# cv2.imshow('OriginalImage', img)
# cv2.imshow('GrayImage', imgGray)
#
# cv2.waitKey(0)

#STEP 2: Image Detection Techniques
#How to blur images
# import cv2
#
# img = cv2.imread('girl.jpeg')
#
# #Convert Image to Gray
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RBG, BGR
#
# #Convert or blurring the image using the "GaussianBlur"
# imgBlur = cv2.GaussianBlur(img,(7,7),0)
#
# cv2.imshow('OriginalImage', img)
# cv2.imshow('GrayImage', imgGray)
# cv2.imshow('BlurImage', imgBlur)

# cv2.waitKey(0)

#STEP 3: Edge Detection

# import cv2
#
# img = cv2.imread('girl.jpeg')
#
# #Convert Image to Gray
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RBG, BGR
#
# #Convert or blurring the image using the "GaussianBlur"
# imgBlur = cv2.GaussianBlur(img,(7,7),0)
#
# #Detecting the edges of the image"
# imgCanny = cv2.Canny(img,200, 200)
#
#
# cv2.imshow('OriginalImage', img)
# cv2.imshow('GrayImage', imgGray)
# cv2.imshow('BlurImage', imgBlur)
# cv2.imshow('CannyImage', imgCanny)
#
# cv2.waitKey(0)

#STEP 4: Dilation and Erode (meaning making edges thicker for dilation and making edges thinner for erode)

import cv2
import numpy as np

img = cv2.imread('girl.jpeg')

#For dilate, we have to specify the kernel
kernel = np.ones((5,5),np.uint8) #unassigned integer 8 bit, meaning values ranging from 0 to 255

#Convert Image to Gray
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #RBG, BGR

#Convert or blurring the image using the "GaussianBlur"
imgBlur = cv2.GaussianBlur(img,(7,7),0)

#Detecting the edges of the image"
imgCanny = cv2.Canny(img,200, 200)

#This enlarges or bold the edges of the image
imgDilation = cv2.dilate(imgCanny, kernel, iterations=4)

#This reduces or erode the edges of the images
imgEroded = cv2.erode(img, kernel, iterations=1)

cv2.imshow('OriginalImage', img)
cv2.imshow('GrayImage', imgGray)
cv2.imshow('BlurImage', imgBlur)
cv2.imshow('CannyImage', imgCanny)
cv2.imshow('DilatedImage', imgDilation)
cv2.imshow('ErodedImage', imgEroded)

cv2.waitKey(0)