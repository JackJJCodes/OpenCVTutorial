import cv2

img = cv2.imread("Resources/cat1.jpeg")

imgResize = cv2.resize(img, (300, 200))
imgCropped = img[0:100, 100:200]  # Image -> Matrix; So we separate segments of the image.

print(img.shape)  # Parameters: Height, width, channel(BGR)
print(imgResize.shape)

cv2.imshow("Image", img)
cv2.imshow("Image-Resized", imgResize)
cv2.imshow("Cropped Image", imgCropped)

cv2.waitKey(0)
