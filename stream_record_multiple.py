import imutils
import time
import cv2
import os
from datetime import datetime

vs = cv2.VideoCapture("nvarguscamerasrc ! video/x-raw(memory:NVMM), width=1200, height=1200, format=(string)NV12, framerate=5/1 ! nvvidconv flip-method=2  ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink") #specific for the Raspberry Pi Camera in Jetson Nano. W, H and framerate are configurable.
writer = None
(W, H) = (None, None)

def recording_loop():
	global writer
	global W
	global H

	while True:
		(grabbed, frame) = vs.read()
		print(frame.shape)
	
		if not grabbed:
			break
	
		if W is None or H is None:
			(H, W) = frame.shape[:2]
	
		if writer is None:
			timestamp=datetime.now()
			fourcc = cv2.VideoWriter_fourcc(*"XVID")
			writer = cv2.VideoWriter(str(timestamp)+".avi", fourcc, 5, (frame.shape[1], frame.shape[0]), True) #it is possible to use ".avi" and others. Framerate has to be the same as above.
	
		writer.write(frame)

		if time.time() > timeout:
			print("End of file "+str(timestamp)) 
			break

while True:
	timeout= time.time() + (10) #time of delay in seconds
	recording_loop()
	writer.release()
	writer = None

