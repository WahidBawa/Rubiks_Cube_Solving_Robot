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

lower_blue = np.array([100, 100, 90])
upper_blue = np.array([114, 245, 200])

lower_green = np.array([54, 194, 72])
upper_green = np.array([80, 255, 225])

lower_white = np.array([83, 0, 114])
upper_white = np.array([151, 156, 187])

lower_yellow = np.array([24, 162, 128])
upper_yellow = np.array([48, 255, 193])

while True:
	_, frame = cap.read()

	# frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	
	width, height = int(cap.get(3)), int(cap.get(4))
	size, space = 50, 90

	masks = [cv2.inRange(hsv, lower_blue, upper_blue),
			 cv2.inRange(hsv, lower_green, upper_green),
			 cv2.inRange(hsv, lower_white, upper_white),
			 cv2.inRange(hsv, lower_yellow, upper_yellow)]
	# mask = cv2.inRange(frame, lower_blue, upper_blue)
	# mask = cv2.inRange(frame,lower_green, upper_green)
	# mask = cv2.inRange(frame, lower_white, upper_white)
	# mask = cv2.inRange(frame, lower_yellow, upper_yellow)
	# mask = cv2.inRange(frame, lower_red, upper_red)

	# result = cv2.bitwise_and(frame,frame,mask = masks[3])
	for i in range(len(masks)):
		result = cv2.bitwise_and(frame,frame,mask = masks[i])
		for x in range(3):
			for y in range(3):
				x1 = int(width / 2 - size / 2 - (size + 40))
				y1 = int(height / 2 - size / 2 - (size + 40))
				x2 = x1 + size
				y2 = y1 + size
				# print(i)
				cv2.rectangle(frame, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
				b = frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][0]
				g = frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][1]
				r = frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][2]
				nb = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][0]
				ng = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][1]
				nr = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][2]
				cv2.imshow('result', result)
				cv2.waitKey(1000)
				# print("OLD:", b, g, r)
				# print("NEW:", result[400][230])
				# print("NEW:", nb, ng, nr)
				# if x == 0 and y == 0:
				# 	cv2.circle(frame, (int(x1 + space * x + size / 2), int(y1 + space * y + size / 2)), 10, (255, 0, 0), 2)
				# 	# cv2.rectangle(result, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
				# elif x == 1 and y == 1:
				# 	cv2.circle(frame, (int(x1 + space * x + size / 2), int(y1 + space * y + size / 2)), 10, (255, 0, 0), 2)
				# 	# cv2.rectangle(result, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
				# 	# cv2.waitKey(1)
				# 	# print(frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)])

				# print(frame[x1 + space * x][y1 + space * y])
	# cv2.imshow('result', result)
	cv2.imshow('frame', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	# if cv2.waitKey(1) & 0xFF == ord('q'):

cv2.destroyAllWindows()