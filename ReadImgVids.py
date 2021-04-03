#  Package for Computer Vision projects:
import cv2

# img = cv2.imread("Resources/lena.png")
#
# cv2.imshow("Lena", img)
#
# cv2.waitKey(0)  # Parameter: Delay

#  For reading a video from device:
# cap = cv2.VideoCapture("Resources/testVideo.mp4")
#
# while True:
#     success, img = cap.read()
#     cv2.imshow("Video", img)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

#  For using web-cam/livefeed:
cap = cv2.VideoCapture(0)  # 0-Webcam, 1- Any other camera connected to the device.
cap.set(3, 640)  # 3: Width
cap.set(4, 480)  # 4: Height
cap.set(10, 100)  # 10: Brightness.


while True:
    success, img = cap.read()
    cv2.imshow("Video", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
