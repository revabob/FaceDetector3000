#!usr/bin/python

import os
import time
import sched
import cv2
import face_recognition
import pickle

s = sched.scheduler(time.time, time.sleep)
cascPath = 'haarcascade_frontalface_default.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
class FaceDetector():

	def __init__(self):
		self.count = 0
		self.face_name = raw_input("Name of Person: ")
		#Tries to create a folder for person whose image dataset is to be generated
		try:
			os.mkdir('./dataset/' + self.face_name)
			print("New Directory created for " + self.face_name)
		#If FileExistsError is generated it is handled below
		except Exception as e:
			print("Dataset for " + self.face_name + " already exists")
			while True:
				choice = raw_input("Press 'q' to quit or 'c' to continue: ")
				if choice == 'q':
					os._exit(0)
				elif choice == 'c':
					break
				else: 
					print("Incorrect input")
			
			
	def save_image(self):
		cv2.imwrite('./dataset/' + self.face_name + '/frame'+str(self.count)+'.png', frame)
		print("[INFO] Frame %d Saved" % self.count)
		self.count += 1
image = FaceDetector()
while True:
# Capture frame-by-frame
	ret, frame = video_capture.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(
        gray,
       	scaleFactor=1.1,
       	minNeighbors=5,
       	minSize=(30, 30),
       	flags=cv2.CASCADE_SCALE_IMAGE
 	)

# Draw a rectangle around the faces
    	for (x, y, w, h) in faces:
	        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the resulting frame
  	cv2.imshow('Video', frame)

  	s.enter(0.2, 1, image.save_image, ())
    	s.run()
    	if cv2.waitKey(1) & 0xFF == ord('q'):
        	break

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
