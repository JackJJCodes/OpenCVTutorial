import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)

while True:
    _, img = cap.read()
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(imgGray, 1.1, 4)

    for (x, y, width, height) in faces:
        cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

    cv2.imshow("Image", img)

    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
