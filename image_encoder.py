import os
import cv2
import face_recognition
import pickle

#Generate a list of the paths of face images
image_locations = []
for dirpath, dirnames, filenames in os.walk("./dataset"):
	for filename in [f for f in filenames if f.endswith(".png")]:
		image_locations.append(os.path.join(dirpath, filename))

#Initialize list of known encodings and names
knownEncodings = []
knownNames = []

for count, image_location in enumerate(image_locations):
	print("[INFO] processing image {}/{}".format(count + 1,len(image_locations)))

	#Find name based on folder name
	name = image_location.split(os.path.sep)[-2]

	#Reads image from image_location	
	image = cv2.imread(image_location)

	#Converts bgr image to rgb format and stores image array in rgb variable
	rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

	#Dectect the cordinates of boxes for each face in rgb image
	boxes = face_recognition.face_locations(rgb, model="hog")

	#Find facial embedding for the face(Converts face to list of 128 numbers)
	encodings = face_recognition.face_encodings(rgb, boxes)
	
	for encoding in encodings:
		knownEncodings.append(encoding)
		knownNames.append(name)
	#Save encodings and names into a file for use in face dection program
	print("\tsaving encoding...")
	data = {"encodings": knownEncodings, "names": knownNames}
	f = open("encodings.pickle", "wb")
	f.write(pickle.dumps(data))
	f.close()
