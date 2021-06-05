import cv2

image = cv2.imread("Resources/cameraman.png")

imageWithText = cv2.putText(image, "CVWeek", (50, 30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)

cv2.imshow("Image With text", imageWithText)

cv2.waitKey(0)
