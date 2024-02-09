#SHAPES AND TEXT
#lines, rectangles, circles, text on images
#create matrix with zeros(0), Zero represent black

# import cv2
# import numpy as np
#
# img = np.zeros((500,500))
# img2 = np.zeros((500,500,3))
# print(img.shape)
# print(img2.shape)
#
# cv2.imshow('img',img)
# cv2.imshow('img2',img)
# cv2.waitKey(0)

#STEP2: Adding color to image

# import cv2
# import numpy as np
#
# img = np.zeros((500,500))
# img2 = np.zeros((500,500,3))
# img3 = np.zeros((500,500,3))
#
# #This colors the image blue following OpenCV BGR
# img2[:] = 255,0,0 #BGR
# #This color a part of the image, blue, by specifying the dimensions/part of the image i.e img3[350:500,0:400]
# img3[350:500,0:400] = 255,0,0 #BGR
#
#
# cv2.imshow('img',img)
# cv2.imshow('img2',img2)
# cv2.imshow('img3',img3)
# cv2.waitKey(0)


#STEP 3: Add line

# import cv2
# import numpy as np
#
# img = np.zeros((500,500,3))
# #cv2.line(img,(100,150),(500,500),(0,0,255),3)
# #Another Form
# cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,0,255),3) #The '3' determine the thickness of the line
#
# cv2.imshow('img',img)
# cv2.waitKey(0)

#STEP 4: Add rectangle#

# import cv2
# import numpy as np
#
# img = np.zeros((500,500,3))
#
# #Another Form
# cv2.rectangle(img,(0,0),(200,350),(0,255,255),1)  #The '1' determine the thickness of the borderline of the rectangle
#
# #This filled the rectangle with the color we have specifiied
# cv2.rectangle(img,(0,0),(200,350),(0,255,255),cv2.FILLED)
#
# cv2.imshow('img',img)
# cv2.waitKey(0)

#STEP 5: Adding a circle and text on the shapes

import cv2
import numpy as np

img = np.zeros((500,500,3))

#Another Form
cv2.circle(img,(250,250),(100),(0,255,255),1)  #The '1' determine the thickness of the borderline of the rectangle
cv2.putText(img,'This is a circle',(200,250),cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0),1)
cv2.imshow('img',img)
cv2.waitKey(0)
