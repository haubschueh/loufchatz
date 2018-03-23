# import the necessary packages
from imutils.video import VideoStream
import datetime
import argparse
import imutils
import time
import cv2
import numpy as np
import sys


PY3 = sys.version_info[0] == 3
if PY3:
    xrange = range


#Var

#Parameter min and max square area
cntMax = 100000
cntMin = 1000

def angle_cos(p0, p1, p2):
    d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
    return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

def find_squares(img):
    img = cv2.GaussianBlur(img, (5, 5), 0)
    squares = []
    for gray in cv2.split(img):
        for thrs in xrange(0, 255, 26):
            if thrs == 0:
                bin = cv2.Canny(gray, 0, 50, apertureSize=5)
                bin = cv2.dilate(bin, None)
            else:
                _retval, bin = cv2.threshold(gray, thrs, 255, cv2.THRESH_BINARY)
            bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
            for cnt in contours:
                cnt_len = cv2.arcLength(cnt, True)
                cnt = cv2.approxPolyDP(cnt, 0.02*cnt_len, True)
                # contourArea(cnt) std = 1000 - see Param
                if len(cnt) == 4 and cv2.contourArea(cnt) > cntMin and cv2.contourArea(cnt) < cntMax and cv2.isContourConvex(cnt):
                    cnt = cnt.reshape(-1, 2)
                    max_cos = np.max([angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                    if max_cos < 0.1:
                        squares.append(cnt)
    return squares

def start_detect():

    vs = VideoStream(usePiCamera=False,resolution=(1920,1080),framerate=21).start()
    time.sleep(2.0)

    count = 0

    while True:
        frame = vs.read()
        squares = find_squares(frame)

        #####  Check if real target found! ####

        #### Check Square in Square ####

        #### Check Square Count ####

        if len(squares) > 4:
            count += 1
            print("Target found! {}".format(count))

        ##### END Checks #####
        #frame = imutils.resize(frame,width=400)
        cv2.drawContours(frame, squares, -1, (0, 255, 0), 3)
        cv2.imshow('squares', frame)
        #time.sleep(0.1)

        # If Target found Break - TBD
        if cv2.waitKey(1) == 13:  # 13 is the Enter Key
            break

    # Release camera and close windows
    vs.stop()
    cv2.destroyAllWindows()
