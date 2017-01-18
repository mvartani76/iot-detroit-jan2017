#!/usr/bin/env/python

# import the necessary packages
import argparse
import datetime
import imutils
import time
import cv2

# Import GPIO/Button functionality
from libsoc_zero.GPIO import Button
from time import sleep

# Import boto S3 functionality
from boto.s3.connection import S3Connection
from boto.s3.key import Key

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Function to upload image to s3 bucket
def upload_image_to_s3(image_file_path, bucket_name):

	"""Uploads images to Amazon's S3 service.

	Arguments:

	image_file_path:	Path to image to upload on local machine.
	bucket_name:		Name of the S3 bucket where file should be uploaded.
	key_name:		Name of the key for the file on S3 (usually the
				timestamp).

	"""
	print("Entered s3 upload...")
	print(bucket_name)
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
	from_:		The Twilio number from which the alert will be sent.
	to:		The phone number that will receive the alert.
	body:		Text for the alert.
	media_url:	The fully qualified path to the image for the alert available
			over the internet.
	"""

	twilio_client.messages.create(from_=from_, to=to, body=body, media_url=media_url)

# Function that is called when motion is detected that uploads file(s) to s3 bucket
# and then sends MMS notifying user of detected motion with an image or images
def send(image_file_paths, s3_bucket):
	media_urls = []

	# loop through the images and create array or media_urls to send to twilio
	for image_file_path in image_file_paths:
		s3_key = upload_image_to_s3(image_file_path, s3_bucket)
	
		media_url = "https://{0}/{1}/{2}".format(REGION_HOST, s3_bucket, s3_key.key)
		print(media_url)
		media_urls.append(media_url)

	send_alert_to_phone_number(twilio_phone_number, verified_phone_number, msg_body, media_urls)
	
# Button Callback function to create new reference frame, firstFrame
def btn_cb():
	# In order to reference the global variable, need to declare callback variable as global
	global firstFrame
	firstFrame = None
	print("Button Pressed!")

btnA = Button("GPIO-A")

btnA.when_pressed(btn_cb)

# Boto S3 Constants
s3_bucket = "your-s3-bucket-name"
aws_access_key_id = "your-aws-access-key-id"
aws_secret_key = "your-aws-secret-key"

# Set the Host to get around 400 Bad Request Error
# Example format something like -> "s3.us-east-2.amazonaws.com"
REGION_HOST = "your-region-host"

# Connect to AWS S3
s3_connection = S3Connection(aws_access_key_id, aws_secret_key, host=REGION_HOST)

# Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

twilio_client = TwilioRestClient(account_sid, auth_token)

# Twilio can only send messages to verified phone numbers with free plan
verified_phone_number = "verified_phone_number"
twilio_phone_number = "twilio_phone_number"
msg_body = "Motion Detected!"
 
# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help="path to the video file")
ap.add_argument("-a", "--min-area", type=int, default=500, help="minimum area size")
args = vars(ap.parse_args())
 
# if the video argument is None, then we are reading from webcam
if args.get("video", None) is None:
	camera = cv2.VideoCapture(0)
	time.sleep(0.25)
 
# otherwise, we are reading from a video file
else:
	camera = cv2.VideoCapture(args["video"])
 
# Initialize the first frame in the video stream
firstFrame = None

# Initialize previous state to "Unoccupied"
prev_state = 0

# Initialize motion timer parameters
MOTION_TIMER_DELAY = 5
motion_timer_start = False
motion_timer = 0

# loop over the frames of the video
while True:
	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = camera.read()
	text = "Unoccupied"
	state = 0
 
	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		break
 
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)

	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue

	# compute the absolute difference between the current frame and
	# first frame
	frameDelta = cv2.absdiff(firstFrame, gray)
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
 
	# loop over the contours
	for c in cnts:
		# if the contour is too small, ignore it
		if cv2.contourArea(c) < args["min_area"]:
			continue
 
		# compute the bounding box for the contour, draw it on the frame,
		# and update the text
		(x, y, w, h) = cv2.boundingRect(c)
		cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		text = "Occupied"
		state = 1

	# draw the text and timestamp on the frame
	cv2.putText(frame, "Room Status: {}".format(text), (10, 20),
		cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
	cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
		(10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
 
	# show the frame and record if the user presses a key
	cv2.imshow("Security Feed", frame)
	cv2.imshow("Thresh", thresh)
	cv2.imshow("First Frame", firstFrame)
	cv2.imshow("Frame Delta", frameDelta)

	# Capture Image if Status changes from Unoccupied to Occupied
	if (state - prev_state) > 0:
		print("Motion Detected")
		img_files = []
		img_file = "img-%s.jpg"%datetime.datetime.now().strftime("%Y%m%d%H%M%S")
		print(img_file)
		img_files.append(img_file)
		cv2.imwrite(img_file, frame)
		motion_timer_start = True

	# Set timer to capture second image after MOTION_TIMER_DELAY frames
	if motion_timer_start:
		if motion_timer == MOTION_TIMER_DELAY:
			img_file = "img-%s.jpg"%datetime.datetime.now().strftime("%Y%m%d%H%M%S")
			img_files.append(img_file)
			cv2.imwrite(img_file, frame)
			send(img_files, s3_bucket)
			motion_timer = 0
			motion_timer_start = False
		motion_timer = motion_timer + 1

	# Store current state into previous state
	prev_state = state

	key = cv2.waitKey(1) & 0xFF
 
	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break
 
# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
btnA.close()
