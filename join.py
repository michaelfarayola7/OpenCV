import cv2
import numpy as np


# # STACKING IMAGES TOGETHER OF 3 CHANNELS / COLOURED IMAGES
# img1 = cv2.imread('girl.jpeg')
# print(img1.shape)
#
# img2 = cv2.imread('boy.jpeg')
# print(img2.shape)
#
#
# #First, match the shape of one of the images to match the other image
# #Here, we are resizing the shape of the second image to match the first which has a shape (172, 183, 3)
# img2Resized = cv2.resize(img2, (183, 172)) # Here, you reverse the shape of img1 to implement on img2
# print(img2Resized)
#
# #Horizontal Stacking
# hstack = np.hstack((img1, img2Resized))
#
# #Vertical Stacking
# vstack = np.vstack((img1, img2Resized))
#
#
# cv2.imshow('horizontalImage', hstack)
# cv2.imshow('verticalImage', vstack)
# cv2.waitKey((0))

#-------------------------------General Function for Stacking Images---------------------------#
# # STACKING IMAGES TOGETHER OF COLOURED IMAGES AND GRAY IMAGES
import cv2
import numpy as np

#Below function is used for stacking images together irrespective of the image channel
def stackImages(scale, imgArray):
 rows = len(imgArray)
 cols = len(imgArray[0])
 rowsAvailable = isinstance(imgArray[0], list)
 width = imgArray[0][0].shape[1]
 height = imgArray[0][0].shape[0]
 if rowsAvailable:
  for x in range(0, rows):
   for y in range(0, cols):
    if imgArray[x][y].shape[:2] == imgArray[0][0].shape[:2]:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (0, 0), None, scale, scale)
    else:
     imgArray[x][y] = cv2.resize(imgArray[x][y], (imgArray[0][0].shape[1], imgArray[0][0].shape[0]), None, scale, scale)
    if len(imgArray[x][y].shape) == 2: imgArray[x][y] = cv2.cvtColor(imgArray[x][y], cv2.COLOR_GRAY2BGR)
  imageBlank = np.zeros((height, width, 3), np.uint8)
  hor = [imageBlank] * rows
  hor_con = [imageBlank] * rows
  for x in range(0, rows):
   hor[x] = np.hstack(imgArray[x])
  ver = np.vstack(hor)
 else:
  for x in range(0, rows):
   if imgArray[x].shape[:2] == imgArray[0].shape[:2]:
    imgArray[x] = cv2.resize(imgArray[x], (0, 0), None, scale, scale)
   else:
    imgArray[x] = cv2.resize(imgArray[x], (imgArray[0].shape[1], imgArray[0].shape[0]), None, scale, scale)
   if len(imgArray[x].shape) == 2: imgArray[x] = cv2.cvtColor(imgArray[x], cv2.COLOR_GRAY2BGR)
  hor = np.hstack(imgArray)
  ver = hor
 return ver




img1 = cv2.imread('girl.jpeg')
img1Gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY) #This convert images to gray

img2 = cv2.imread('boy.jpeg')
img2Gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY) #This convert images to gray


#Here we called the function "stackImages"
#For Horizontal stacking, you put all images in a list
#For vertical stacking, put all the images in two or more list in your function call
imagStack = stackImages(1, ([img1, img2, img1Gray],[ img2, img2Gray, img1]))

cv2.imshow('stackImage', imagStack)
#cv2.imshow('verticalImage', vstack)

cv2.waitKey((0))

