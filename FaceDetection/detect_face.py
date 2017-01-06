#!/usr/bin/env python
import cv2, sys

# Define constants
DEVICE_NUMBER = 0

# Get XML file input
if len(sys.argv) > 1:
	XML_PATH = sys.argv[1]
else:
	print "Error: XML path not defined"
	sys.exit(1)

# Initialize the cascade classifier
print "Initializing cascade filter"
faceCascade = cv2.CascadeClassifier(XML_PATH)

# Initialize webcam
print "Initializing webcam"
vc = cv2.VideoCapture(DEVICE_NUMBER)

# Check if the webcam works
if vc.isOpened():
	# Try to get the first frame
	retval, frame = vc.read()
else:
	# Exit the program
	print "Webcam does not work..."
	sys.exit(1)

i= 0
faces = []

# If the webcam read is successful, loop indefinitely
while retval:
	# Define the frame which the program will show
	frame_show = frame

	if i % 5 == 0:
		# Convert frame to grayscale to perform facial detection
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

		# Detect objects and return an array of faces
		faces = faceCascade.detectMultiScale(
			frame,
			scaleFactor=1.2,
			minNeighbors=2,
			minSize=(50, 50),
			flags=cv2.cv.CV_HAAR_SCALE_IMAGE
		)

	# Draw a rectangle around the faces
	for (x, y, w, h) in faces:
		cv2.rectangle(frame_show, (x, y), (x+w, y+h), (0, 0, 255), 2)

	# Show the frame on the screen
	cv2.imshow("DragonBoard 410c Workshop", frame_show)

	# Read in the next frame
	retval, frame = vc.read()

	# Exit program if the ESCAPE key is pressed
	if cv2.waitKey(1) == 27:
		breal

	i += 1


