import time
import cv2
import face_recognition
import pickle

#Load encoding obtained from image encoder
data = pickle.loads(open("encodings.pickle", "rb").read())

#Start video stream
video_capture = cv2.VideoCapture(0)

while True:
	# Capture frame-by-frame
	ret, frame = video_capture.read()
	rgb = cv2.resize(frame, (750,frame.shape[1]))
	rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	r = frame.shape[1] / float(rgb.shape[1])
	boxes = face_recognition.face_locations(rgb, model="hog")
	encodings = face_recognition.face_encodings(rgb, boxes)
	names = []
	# loop over the facial embeddings
	for encoding in encodings:
		# attempt to match each face in the input image to our known encodings
		matches = face_recognition.compare_faces(data["encodings"],
			encoding)
		#If face detected is other than the faces in dataset assign name as empty string
		name = ""
 
		# check to see if we have found a match
		if True in matches:
			# find the indexes of all matched faces then initialize a
			# dictionary to count the total number of times each face
			# was matched
			matchedIdxs = [i for (i, b) in enumerate(matches) if b]
			counts = {}
 
			# loop over the matched indexes and maintain a count for
			# each recognized face face
			for i in matchedIdxs:
				name = data["names"][i]
				counts[name] = counts.get(name, 0) + 1
 
			# determine the recognized face with the largest number
			# of votes (note: in the event of an unlikely tie Python
			# will select first entry in the dictionary)
			name = max(counts, key=counts.get)
		
		# update the list of names
		names.append(name)
		# loop over the recognized faces
	for ((top, right, bottom, left), name) in zip(boxes, names):
		# rescale the face coordinates
		top = int(top * r)
		right = int(right * r)
		bottom = int(bottom * r)
		left = int(left * r)
		y = top - 2
		#Colorize text background and write name of face detected
 		(text_width, text_height) = cv2.getTextSize(name, cv2.FONT_HERSHEY_PLAIN, fontScale=1.5, thickness=1)[0]
		#Check if face detected is not in training dataset 
		if name != "":
			box_coords = ((left-1, y), (left + text_width, y - text_height-4))
			cv2.rectangle(frame, box_coords[0], box_coords[1], (0,255,0), cv2.FILLED)
			cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX,0.75, (0, 0, 0), 2)
		
		# draw box around predicted face on the image
		cv2.rectangle(frame, (left, top), (right, bottom),(0, 255, 0), 2)
      
	cv2.namedWindow("Video", cv2.WINDOW_NORMAL)
	cv2.imshow("Video", frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
	#Future Expansion
	'''if "Revanth" in names:
		time.sleep(2)
		print("Revanth Detected\nDisabling Lock...\nWelcome Back Boss!")
		break'''
video_capture.release()
cv2.destroyAllWindows()	
