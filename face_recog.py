import time
import cv2
import numpy as np
import sys

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cam = cv2.VideoCapture(0)
ret,img = cam.read()

name = raw_input('Enter user name for dataset')
img_number = 0
while True:
    # Capture frame-by-frame
    ret, img = cam.read()

    t1=time.time()
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Output', img)

    print(time.time()-t1)

    if(img_number > 20):
          break
    if cv2.waitKey(33) & 0xFF == 27:
        break
cam.release()
cv2.destroyAllWindows()
