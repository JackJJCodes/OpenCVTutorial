import cv2

path = "Resources/lena.png"

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread(path)
imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(imgGray, 1.1, 4)

# Creating bounding boxes around faces:
for (x, y, width, height) in faces:
    cv2.rectangle(img, (x, y), (x + width, y + height), (255, 0, 0), 2)

cv2.imshow("Original Image", img)
cv2.waitKey(0)
