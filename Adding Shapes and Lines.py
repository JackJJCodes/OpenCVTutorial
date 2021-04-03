import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)  # Image filled with black; 0->black
# print(img.shape)
# img[:] = 255, 0, 0  # Making the image blue.

#  If we want to make a specific part of the image BLUE, we can crop and apply as done in the last chapter:
#  img[200:300, 100:300] = 255, 0, 0

# cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3)  # Parameters: image ; startpoint ; endpoint ; thickness

# For creating a diagonal line:
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)

# For creating a rectangle:
cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), 2)
# To fill our rectangle:
# cv2.rectangle(img, (0, 0), (250, 350), (0, 0, 255), cv2.FILLED)

# For creating a circle:
cv2.circle(img, (400, 50), 30, (255, 255, 0), 5)

# for putting text:
cv2.putText(img, "CV Week!!", (300, 150), cv2.FONT_HERSHEY_DUPLEX, 1, (0, 150, 0), 1)

cv2.imshow("Image", img)

cv2.waitKey(0)
