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
			x, y = 0, 0
			# x1 = int(width / 2 - size / 2 - (size + 40))
			# y1 = int(height / 2 - size / 2 - (size + 40))
			x1 = 70
			y1 = 163
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