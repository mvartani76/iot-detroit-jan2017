# Motion Detection
Repository for Motion Detector Code

##motion_detector_static_ref.py
The source for this code is a tutorial from Adrian Rosebrock @ pyimagesearch about installing a simple motion detection algorithm using OpenCV on a Raspberry Pi. The tutorial is located at the URL, http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/.

The overly simplified basis for the motion detection in this code is background subtraction using a reference frame. The code calculates the pixel differences between the current frame and the reference frame, compares it to a threshold to determine if there is motion.

This code makes the assumption that the first frame of our video file will contain no motion and just background — therefore, we can model the background of our video stream using only the first frame of the video. As we can probably guess with a live webcam, this is probably not going to be true if we run the code sitting in front of the webcam as I did many times. Changes in lighting and shadows will also cause issues to this but this is a simple algorithm to show what could potentially be accomplished.
