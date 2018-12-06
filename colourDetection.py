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

	
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	width, height = int(cap.get(3)), int(cap.get(4))
	size, space = 50, 90

	masks = [cv2.inRange(hsv, lower_blue, upper_blue),
			 cv2.inRange(hsv, lower_green, upper_green),
			 cv2.inRange(hsv, lower_white, upper_white),
			 cv2.inRange(hsv, lower_yellow, upper_yellow)]
	result = cv2.bitwise_and(frame,frame,mask = masks[1])
	# for i in range(0):#	len(masks)):
	# gray = cv2.cvtColor(result, cv2.COLOR_BGR2GRAY)
	# gray = np.float32(gray)

	# corners = cv2.goodFeaturesToTrack(gray, 36, 0.01, 10)
	# corners = np.int0(corners)

	# for corner in corners:
	#     x,y = corner.ravel()
	#     cv2.circle(frame,(x,y),3,255,-1)
	
	# cv2.imshow('Corner', frame)
	for x in range(3):
		for y in range(3):
			x1 = int(width / 2 - size / 2 - (size + 40))
			y1 = int(height / 2 - size / 2 - (size + 40))
			x2 = x1 + size
			y2 = y1 + size
			cv2.rectangle(frame, (x1 + space * x, y1 + space * y), (x2 + space * x, y2 + space * y), (255, 0, 255), 3)
			l1 = lower_green[0]
			l2 = lower_green[1]
			l3 = lower_green[2]

			u1 = upper_green[0]
			u2 = upper_green[1]
			u3 = upper_green[2]
			
			b = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][0]
			g = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][1]
			r = result[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][2]
			print(b, g, r)
			if x == 1 and y == 1:
				if b > l1:
					if g > l2:
						if r > l3:
							if b < u1:
								if g < u2:
									if r < u3:
										cv2.circle(frame, (int(x1 + space * x + size / 2), int(y1 + space * y + size / 2)), 10, (255, 0, 0), 2)
										print(frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)])
										cv2.destroyAllWindows()
				# print(frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][0] > lower_yellow[0], frame[int(x1 + space * x + size / 2)][int(y1 + space * y + size / 2)][0] < upper_yellow[0])

			# print(frame[x1 + space * x][y1 + space * y])
	cv2.imshow('result', result)
	cv2.imshow('frame', frame)
	k = cv2.waitKey(5) & 0xFF
	if k == 27:
		break
	# if cv2.waitKey(1) & 0xFF == ord('q'):

cv2.destroyAllWindows()