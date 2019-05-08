#!usr/bin/python

import os
import time

def display_title():

	os.system('clear')
	print("#####################################################\n")
	print("########          Face Detector 3000          #######\n")
	print("#####################################################\n")	

def display_options():	
	
	print("[1] Run Face Detector")
	print("[2] Create Dataset")
	print("[3] Encode Dataset")
	print("[q] Quit")

while True:
		
	display_title()
	display_options()
	choice = raw_input("Enter choice: ")
	if choice == '1':
		display_title()
		print("[INFO] Starting camera...")
		print("[INFO] Activating face detector...")
		os.system("python face_detector3000.py")
	elif choice == '2':
		display_title()
		print("Initializing...")
		os.system("python image_dataset_generator.py")

	elif choice == '3':
		os.system("python image_encoder.py")
	elif choice == 'q':
		os.system('clear')
		os._exit(0)
	else:
		
		print("Incorrect choice. Try again")
		time.sleep(2)
				
		
