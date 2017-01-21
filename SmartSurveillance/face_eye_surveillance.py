#!/usr/bin/env/python

# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2
import sys

# Import boto S3 functionality
from boto.s3.connection import S3Connection

from boto.s3.key import Key

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Function to upload image to s3 bucket
def upload_image_to_s3(image_file_path, bucket_name):

	"""Uploads images to Amazon's S3 service.

	Arguments:

	image_file_path: Path to image to upload on local machine.
	bucket_name: Name of the S3 bucket where file should be uploaded.
	key_name: Name of the key for the file on S3 (usually the
			timestamp).

	"""
	print("Entered s3 upload...")
	print(bucket_name)
	print(image_file_path)
	bucket = s3_connection.get_bucket(bucket_name)

	# Create a new key using image_file_path as the key

	key = Key(bucket)
	key.key = image_file_path 
	key.set_contents_from_filename(image_file_path)

	return key

# Send Alert to Phone Number Using Twilio
def send_alert_to_phone_number(from_=None, to=None, body=None, media_url=None):
	""" Sends a MMS using Twilio.

	Arguments:
	from_: The Twilio number from which the alert will be sent.
	to: The phone number that will receive the alert.
	body: Text for the alert.
	media_url: The fully qualified path to the image for the alert available
		over the internet.
	"""

	twilio_client.messages.create(from_=from_, to=to, body=body, media_url=media_url)

# Function that is called when motion is detected that uploads file(s) to s3 bucket
# and then sends MMS notifying user of detected motion with an image or images
def send(image_file_path, s3_bucket):
	media_urls = []

	# loop through the images and create array or media_urls to send to twilio
	s3_key = upload_image_to_s3(image_file_path, s3_bucket)
	
	media_url = "https://{0}/{1}/{2}".format(REGION_HOST, s3_bucket, s3_key.key)
	print(media_url)
	media_urls.append(media_url)

	send_alert_to_phone_number(twilio_phone_number, verified_phone_number, msg_body, media_urls)

# Boto S3 Constants
s3_bucket = "your-s3-bucket-name"
aws_access_key_id = "your-aws-access-key-id"
aws_secret_key = "your-aws-secret-key"

# Set the Host to get around 400 Bad Request Error
# Example format something like -> "s3.us-east-2.amazonaws.com"
REGION_HOST = "your-region-host"

# Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

twilio_client = TwilioRestClient(account_sid, auth_token)

verified_phone_number = "verified_phone_number"
twilio_phone_number = "twilio_phone_number"
msg_body = "Face Detected!"

s3_connection = S3Connection(aws_access_key_id, aws_secret_key, host=REGION_HOST)

# Define constants
DEVICE_NUMBER = 0

# Get XML file input
if len(sys.argv) > 1:
	FACE_XML_PATH = sys.argv[1]
	EYE_XML_PATH = sys.argv[2]
else:
	print "Error: XML path not defined"
	sys.exit(1)

# Initialize the cascade classifier
print "Initializing cascade filter"
faceCascade = cv2.CascadeClassifier(FACE_XML_PATH)
eyeCascade = cv2.CascadeClassifier(EYE_XML_PATH)

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
prev_state = 0

# If the webcam read is successful, loop indefinitely
while retval:
	# Define the frame which the program will show
	frame_show = frame

	state = 0

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
		if len(faces) == 1:
		# Draw a rectangle around the faces
			for (x, y, w, h) in faces:
				cv2.rectangle(frame_show, (x, y), (x+w, y+h), (0, 0, 255), 2)
				roi_frame = frame_show[y:y+h, x:x+w]
				eyes = eyeCascade.detectMultiScale(roi_frame)
				for (ex, ey, ew, eh) in eyes:
					cv2.rectangle(roi_frame, (ex, ey), (ex+ew, ey+eh), (0,255,0), 2)
				if len(eyes) == 2:
					state = 1
					if (state - prev_state) > 0:
						img_file = "img-%s.jpg"%datetime.datetime.now().strftime("%Y%m%d%H%M%S")
						cv2.imwrite(img_file, frame)
						send(img_file, s3_bucket)
				else:
					state = 0

	# Store current state into previous state
	prev_state = state

	# Show the frame on the screen
	cv2.imshow("DragonBoard 410c Workshop", frame_show)

	# Read in the next frame
	retval, frame = vc.read()

	# if the `q` key is pressed, break from the loop
	key = cv2.waitKey(1) & 0xFF
	if key == ord("q"):
		break

	i += 1

vc.release()
cv2.destroyAllWindows()
