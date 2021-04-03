import cv2
import numpy as np

img = cv2.imread('Resources/cards.jpg')

width, height = 250, 350  # Standard playing cards size
# Trying to ge the second card:
points1 = np.float32([[223, 19], [386, 24], [389, 281], [216, 279]])  # going clockwise; start: top-left
points2 = np.float32([[0, 0], [width, 0], [width, height], [0, height]])
matrix = cv2.getPerspectiveTransform(points1, points2)
imgOutput = cv2.warpPerspective(img, matrix, (width, height))

cv2.imshow("Cards", img)
cv2.imshow("Output", imgOutput)

cv2.waitKey(0)
