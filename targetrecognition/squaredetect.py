# import the necessary packages
#from imutils.video import VideoStream
from targetrecognition.videostream import VideoStream
import time
import cv2
import numpy as np




#PY3 = sys.version_info[0] == 3
#if PY3:
xrange = range

class SquareDetect:


    def __init__(self):

        self.videoStream = VideoStream(usePiCamera=True,resolution=(1280,720),framerate=21).start()

        #Parameter min and max square area
        self.cntMax = 1000000
        self.cntMin = 1000
        self.approxSq = 0.01

    def angle_cos(self,p0, p1, p2):
        d1, d2 = (p0-p1).astype('float'), (p2-p1).astype('float')
        return abs( np.dot(d1, d2) / np.sqrt( np.dot(d1, d1)*np.dot(d2, d2) ) )

    def find_squares(self, img):
        squares = []

        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        img = cv2.GaussianBlur(img, (5, 5), 0)

        ret, bin = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

        bin, contours, _hierarchy = cv2.findContours(bin, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            cnt_len = cv2.arcLength(cnt, True)
            #Stadard value (cnt, 0.02*cnt_len, True)
            cnt = cv2.approxPolyDP(cnt, self.approxSq*cnt_len, True)
            # contourArea(cnt) std = 1000 - see Param
            if len(cnt) == 4 and cv2.contourArea(cnt) > self.cntMin and cv2.contourArea(cnt) < self.cntMax and cv2.isContourConvex(cnt):
                cnt = cnt.reshape(-1, 2)
                max_cos = np.max([self.angle_cos( cnt[i], cnt[(i+1) % 4], cnt[(i+2) % 4] ) for i in xrange(4)])
                if max_cos < 0.1:
                    squares.append(cnt)
        return squares

    def start_detect(self):
        self.videoStream = VideoStream(usePiCamera=True,resolution=(1280,720),framerate=21).start()
        time.sleep(2.0)

        sucess = False
        count = 0

        while True:
            frame = self.videoStream.read()
            squares = self.find_squares(frame)

            # Check contour count in parrent contour
            if len(squares) > 4:
                count += 1
                print("Target found! {}".format(count))
                sucess = True

            # Speed Test
            count += 1
            #print("new Frame")
            #print(count)

            # If Target found Break - TBD
            if sucess or cv2.waitKey(1) == 13:  # 13 is the Enter Key
                break

        # Release camera
        self.videoStream.stop()

        return frame, squares
