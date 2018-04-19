from squaredetect import SquareDetect
from squarecheck import SquareCheck
import cv2

class TargetRec:

    def __init__(self):

        self.sd = SquareDetect()
        self.sc = SquareCheck()
        self.target = 0
        self.last_frame = 0

    def searchSquare(self):

        frame, squares = self.sd.start_detect()
        sorted_squares = sorted(squares, key=cv2.contourArea, reverse=False)
        self.target = sorted_squares
        self.last_frame = frame

        return frame, squares

    def getTargetPos(self):
        first_sq = self.target[0]
        M = cv2.moments(first_sq)
        cx = int(M['m10'] / M['m00'])
        cy = int(M['m01'] / M['m00'])

        return cx, cy

    def getTestPicture(self):
        cx, cy = self.getTargetPos()
        frame = self.last_frame
        cv2.circle(frame, (cx, cy), 2, (0, 0, 255), -1)

        height, width = frame.shape[:2]

        cv2.drawContours(frame, self.target, -1, (0, 255, 0), 3)

        print("Target found!")
        print("An der Position x=" + str(cx) + " und y=" + str(cy))
        print("Bild Höhe: " + str(height) + "  Bild Weite: " + str(width))

        return frame

    def testGetSquareArea(self):
        index = len(self.target)
        out_square = self.target[index-1]

        print(out_square)

        square = out_square

        low_point_x = 50000
        low_point_y = 50000
        max_point_x = 0
        max_point_y = 0
        for i in range(4):
            for k in range(2):
                if square[i][k] < low_point_x and k==0:
                    low_point_x = square[i][k]
                if square[i][k] < low_point_y and k == 1:
                    low_point_y = square[i][k]


                if square[i][k] > max_point_x and k==0:
                    max_point_x = square[i][k]
                if square[i][k] > max_point_y and k == 1:
                    max_point_y = square[i][k]

        print(low_point_x)
        print(low_point_y)
        print(max_point_x)
        print(max_point_y)

        p1 = square[0]
        p2 = square[1]
        p3 = square[2]
        p4 = square[3]

        #Temp Test:
        frame = self.last_frame
        cv2.circle(frame, (low_point_x, low_point_y), 2, (0, 0, 255), -1)
        cv2.circle(frame, (max_point_x, max_point_y), 2, (0, 0, 255), -1)
        # Temp Test:
        #cv2.circle(frame, (p1[0], p1[1]), 2, (0, 0, 255), -1)
        #cv2.circle(frame, (p2[0], p2[1]), 2, (0, 0, 255), -1)
        #cv2.circle(frame, (p3[0], p3[1]), 2, (0, 0, 255), -1)
        #cv2.circle(frame, (p4[0], p4[1]), 2, (0, 0, 255), -1)

        cv2.imshow("Show Points Square Area", frame)

        return p1,p2,p3,p4

    def getSquareArea(self):
        index = len(self.target)
        square = self.target[index-1]


        low_point_x = 50000
        low_point_y = 50000
        max_point_x = 0
        max_point_y = 0
        for i in range(4):
            for k in range(2):
                if square[i][k] < low_point_x and k==0:
                    low_point_x = square[i][k]
                if square[i][k] < low_point_y and k == 1:
                    low_point_y = square[i][k]


                if square[i][k] > max_point_x and k==0:
                    max_point_x = square[i][k]
                if square[i][k] > max_point_y and k == 1:
                    max_point_y = square[i][k]


        return low_point_x,low_point_y,max_point_x,max_point_y

    def checkTarget(self):
        p1,p2,p3,p4 = self.getSquareArea()

        t_l_x = p1
        t_l_y = p1
        b_r_x = p4
        b_r_y = p4

        return self.sc.siftCheck(t_l_x,t_l_y,b_r_x,b_r_y)


