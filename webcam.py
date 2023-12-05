# Tis code is for opening the webcam

import cv2
import matplotlib as plt

video = cv2.VideoCapture(0)

while video.isOpened():
    # Show image
    ret, frame = video.read()
    cv2.imshow('Webcam', frame)

    # Stop button
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video.release()
cv2.destroyAllWindows()
