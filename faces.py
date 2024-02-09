#STEP 1: Face detection in images

# import cv2
#
#
# facescascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
# img = cv2.imread('face.jpeg')
#
# imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# faces = facescascade.detectMultiScale(img,1.1,4)
#
# for (x,y,w,h) in faces:
#     cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
#
#
# cv2.imshow('girlface',img)
# cv2.waitKey(0)



##--------------------------------------Face Detection in Video------------------------------##



# import cv2
#
# # Load the cascade
# faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')
#
# # To capture video from webcam
# cap = cv2.VideoCapture(0)
#
# while True:
#     # Read the frame
#     _, img = cap.read()
#
#     # Convert to grayscale
#     imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#
#     # Detect faces
#     faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
#
#     # Draw rectangle around the faces
#     for (x, y, w, h) in faces:
#         cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
#
#     # Display
#     cv2.imshow('Video', img)
#
#     # Stop if escape key is pressed
#     k = cv2.waitKey(1) & 0xff
#     if k == ord('q'):  # Use 'q' to quit the program
#         break

# # Release the VideoCapture object and close the windows
# cap.release()
# cv2.destroyAllWindows()




#-------------------------Another Form-----------------------#

import cv2

# Load the cascade
faceCascade = cv2.CascadeClassifier('haarcascades/haarcascade_frontalface_default.xml')

# To capture video from webcam
cap = cv2.VideoCapture('faces.mp4')

while True:
    # Read the frame
    success, img = cap.read()

    if not success:
        break  # If no frame is read, break out of the loop

    # Convert to grayscale, detect faces, draw rectangles, and display the frame
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
    cv2.imshow('Video', img)

    # Stop if 'q' is pressed
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
