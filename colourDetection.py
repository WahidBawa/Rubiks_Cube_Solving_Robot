#colourDetection.py
import numpy as np
import cv2
# img = cv2.imread('pic.jpg')
# cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?320x240")

# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?320x240")

# cap = cv2.VideoCapture("http://10.42.0.21:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://10.42.0.21:4747/mjpegfeed?320x240")

# cap = cv2.VideoCapture("http://10.42.0.248:8080/video")
cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:8080/video")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")
while True:

	WHITE = [200, 200, 200]
	BLUE = [125, 76, 22]
	YELLOW = [200, 200, 200]
	GREEN = [62, 87, 15]
	ORANGE = [200, 200, 200]
	RED = [53, 53, 140]

	_, frame = cap.read()

	# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	# mask = cv2.inRange(frame, (0, 150,0), (100, 255, 40)) #green
	mask = cv2.inRange(frame, (0, 0, 200), (10, 40, 250)) #orange
	res = cv2.bitwise_and(frame,frame, mask= mask)

	# cv2.imshow('frame',frame)
	# cv2.imshow('mask',mask)
	# cv2.imshow('res',res)

	width, height = int(cap.get(3)), int(cap.get(4))
	size, space = 50, 90
	for x in range(3):
		for y in range(3):
			x1 = int(width / 2 - size / 2 - (size + 40))
			y1 = int(height / 2 - size / 2 - (size + 40))
			x2 = x1 + size
			y2 = y1 + size
			# cv2.rectangle(frame, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
			cv2.rectangle(res, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
	
	# cv2.imshow('Corner', frame)
	cv2.imshow('res',res)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cv2.destroyAllWindows()