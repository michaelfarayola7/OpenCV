import cv2
import numpy as np

img = cv2.imread('card.jpeg')

#Here, we need to specify the normal playing card dimensions
width,height = 250,350


#pts1: This specifies the four coordinates of the part or feature of an image we want to extra
#pts2: This what each of those number or coordinates mean
pts1 = np.float32([[231,58],[342,50],[252,218],[371,208]]) #https://www.mobilefish.com/services/record_mouse_coordinates/record_mouse_coordinates.php
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])


#Calculates the transformation matrix required to transform the points from pts1 to their new positions in pts2.
matrix = cv2.getPerspectiveTransform(pts1,pts2)

#Applies the perspective transformation to the entire image using the transformation matrix calculated in the previous step.
imgOutput = cv2.warpPerspective(img, matrix,(width,height))
cv2.imshow('card', img)
cv2.imshow('cardOutput', imgOutput)
cv2.waitKey(0)
