from targetrec import TargetRec
import imutils
import cv2
import time


tr = TargetRec()

frame, squares = tr.searchSquare()

frame2 = tr.getTestPicture()

cv2.imshow("Test Found Target", frame2)

#sucess = tr.checkTarget()

#p1,p2,p3,p4 = tr.getSquareArea()

test = tr.checkTarget()

while True:


    # If Target found Break - TBD
    if cv2.waitKey(1) == 13:  # 13 is the Enter Key
        break

# Release camera and close windows
cv2.destroyAllWindows()
