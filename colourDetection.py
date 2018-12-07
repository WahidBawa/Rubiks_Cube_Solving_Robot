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

cap = cv2.VideoCapture("http://10.42.0.248:8080/video")
# cap = cv2.VideoCapture("http://10.42.0.248:4747/mjpegfeed?640x480")
# cap = cv2.VideoCapture("http://192.168.0.75:8080/video")
# cap = cv2.VideoCapture("http://192.168.0.75:4747/mjpegfeed?640x480")

# lower_blue = np.array([100, 100, 90])
# upper_blue = np.array([114, 245, 200])
lower_blue = np.array([106, 179, 54])
upper_blue = np.array([125, 241, 98])

lower_green = np.array([54, 194, 72])
upper_green = np.array([80, 255, 225])

lower_white = np.array([83, 0, 114])
upper_white = np.array([151, 156, 187])

lower_yellow = np.array([29, 164, 110])
upper_yellow = np.array([38, 255, 170])

while True:
	_, frame = cap.read()

	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	width, height = int(cap.get(3)), int(cap.get(4))

	masks = [cv2.inRange(hsv, lower_blue, upper_blue),
			 cv2.inRange(hsv, lower_green, upper_green),
			 cv2.inRange(hsv, lower_white, upper_white),
			 cv2.inRange(hsv, lower_yellow, upper_yellow)]
	mask = masks[3]
	result = cv2.bitwise_and(frame,frame,mask = mask)
	size, space = 50, 80
	for x in range(3):
		for y in range(3):
			# x, y = 0, 2
			x1 = int(width / 2 - size / 2 - (size + 40))
			y1 = int(height / 2 - size / 2 - (size + 40))
			x2 = x1 + size
			y2 = y1 + size
			cv2.rectangle(frame, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 0), 3)

			# b = mask[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)]
			b = mask[int(x1 + space * x)][int(y1 + space * y)]
			# b = int(b)
			print(x, y, b)
			# g = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][1]
			# r = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][2]
			if b == 255:
				cv2.circle(frame, (int(x1 + space * x + size / 2), int(y1 + space * y + size / 2)), 15, (255, 0, 255), 3)
				print("maybe worker")
				# cv2.rectangle(frame, (x1 + space * varx, y1 + space * vary), (x2 + space * varx, y2 + space * vary), (255, 0, 255), 3)
			# print(frame[x1 + space * x][y1 + space * y])

	# cv2.imshow('result', result)
	cv2.imshow('mask', mask)
	cv2.imshow('frame', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
cv2.destroyAllWindows()