import cv2
#
# print('Package imported')
#
# #STEP 1
# #reading images

# # use imread to read images
# # use "imshow" to display the images, however, you need to specify a name for the image to show
# # Also, we need to specify a waitKey to visualize the image for sometimes.
# # Press "Q" to quit image display
# # ###
#
# img = cv2.imread('boy.jpeg')
# cv2.imshow('girl image',img)
#
# cv2.waitKey(5000)


# #STEP 2: Streaming Video

# use "VideoCapture" to capture the images in the video and store in a variable
# implement a while loop to read the different images in the stored variable
# implement a waitKey in an 'if' statement where the press of 'q' can be used to quit the video

# cap = cv2.VideoCapture("video.mp4")
# while True:
#     success, img = cap.read()
#     cv2.imshow('girlImage', img)
#     if cv2.waitKey(19) & 0xFF ==ord('q'):
#         break

# # STEP 3: Streaming from WebCam

# use "VideoCapture" to capture the images in the video and store in a variable
# implement a while loop to read the different images in the stored variable
# implement a waitKey in an 'if' statement where the press of 'q' can be used to quit the video

cap = cv2.VideoCapture(0)
cap.set(3,640) #Sets the width of the video frame to 640 pixels
cap.set(4, 480) #Sets the height of the video frame to 480 pixels
cap.set(10, 255) #Attempts to set the brightness of the video, as brightness values fall within (0-255 for many cameras)
while True:
    success, img = cap.read()
    cv2.imshow('webcamVideo', img)
    if cv2.waitKey(19) & 0xFF ==ord('q'):
        break

