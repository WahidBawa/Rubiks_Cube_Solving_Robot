import cv2
import numpy as np


cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?320x240")

# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?320x240")

# cap = cv2.VideoCapture("http://10.42.0.21:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://10.42.0.21:4747/mjpegfeed?320x240")

cap = cv2.VideoCapture("http://10.42.0.248:8080/video")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:8080/video")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking

h,s,v = 180,255,255
# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)

cv2.createTrackbar('h2', 'result',0,179,nothing)
cv2.createTrackbar('s2', 'result',0,255,nothing)
cv2.createTrackbar('v2', 'result',0,255,nothing)


while(True):

    _, frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')

    h2 = cv2.getTrackbarPos('h2','result')
    s2 = cv2.getTrackbarPos('s2','result')
    v2 = cv2.getTrackbarPos('v2','result')

    lower_blue = np.array([109, 86, 50])
    upper_blue = np.array([138, 238, 217])

    lower_green = np.array([42, 162, 101])
    upper_green = np.array([74, 255, 200])

    lower_white = np.array([0, 0, 223])
    upper_white = np.array([179, 28, 255])

    lower_yellow = np.array([23, 123, 193])
    upper_yellow = np.array([36, 255, 255])

    lower_red = np.array([0, 194, 162])
    upper_red = np.array([2, 255, 255])

    lower_orange = np.array([3, 205, 209])
    upper_orange = np.array([10, 255, 255])
    # lower_red = np.array([h, s, v])
    # upper_red = np.array([h2, s2, v2])

    # mask = cv2.inRange(hsv, lower_blue, upper_blue)
    # mask = cv2.inRange(hsv,lower_green, upper_green)
    # mask = cv2.inRange(hsv, lower_white, upper_white)
    # mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
    # mask = cv2.inRange(hsv, lower_red, upper_red)
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    

    # result = cv2.bitwise_and(frame,frame,mask = mask)
    result = cv2.bitwise_and(frame,frame,mask = mask)

    width, height = int(cap.get(3)), int(cap.get(4))
    size, space = 50, 80
    for x in range(3):
        for y in range(3):
            x1 = int(width / 2 - size / 2 - (size + 40))
            y1 = int(height / 2 - size / 2 - (size + 40))
            x2 = x1 + size
            y2 = y1 + size
            # cv2.rectangle(frame, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
            # cv2.rectangle(result, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
    
    # cv2.imshow('Corner', frame)
    # cv2.imshow('res',res)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        print("Min HSV:", h, s, v)
        print("Max HSV:", h2, s2, v2)
        break

cap.release()

cv2.destroyAllWindows()