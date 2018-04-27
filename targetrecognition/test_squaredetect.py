from squaredetect import SquareDetect
import imutils
import cv2
import time


sd = SquareDetect()

frame, squares = sd.start_detect()


while True:


    cv2.drawContours(frame, squares, -1, (0, 255, 0), 3)
    cv2.imshow('squares', frame)

    # If Target found Break - TBD
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# Release camera and close windows
cv2.destroyAllWindows()
