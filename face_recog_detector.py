import time
import cv2
import sqlite3 as sql
import numpy as np
import sys
import os

faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
cam = cv2.VideoCapture(0)
rec = cv2.createLBPHFaceRecognizer()
rec.load('trainingDataset.yml')
id = 0
font = cv2.FONT_HERSHEY_SIMPLEX

conn = sql.connect('test.db')
c = conn.cursor()

while True:
    ret, img = cam.read()
    t1=time.time()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=5,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        id,conf = rec.predict(gray[y:y+h,x:x+w])
        c = c.execute("SELECT * FROM Facedetails WHERE id = " + str(id))
        for row in c:
            cv2.putText(img, 'Id : '+str(row[0]), (x, y + h + 10), font, 0.5, (200, 255, 255), 1)
            cv2.putText(img, 'Name : '+str(row[1]), (x, y + h + 25), font, 0.5, (200, 255, 255), 1)
            cv2.putText(img, 'Age : '+str(row[2]), (x, y + h + 37), font, 0.5, (200, 255, 255), 1)
            cv2.putText(img, 'conf : '+ str(conf), (x, y + h + 50), font, 0.5, (200, 255, 255), 1)
    cv2.imshow('Output', img)
    print(time.time()-t1)
    if cv2.waitKey(33) & 0xFF == 27:
        break
cam.release()
cv2.destroyAllWindows()
