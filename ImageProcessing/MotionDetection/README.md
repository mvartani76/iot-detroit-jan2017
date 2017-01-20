#Motion Detection
This repository contains information and example code on how to perform motion detection using various background subtraction techniques.

##Pre-requisites
Need to install `imutils` in order to use some of the convenience functions in the code below.

```
pip install imutils
```
The source github for this code is located here: https://github.com/jrosebr1/imutils

##Background/Code Source
The source for this code is a tutorial from Adrian Rosebrock @ pyimagesearch about installing a simple motion detection algorithm using OpenCV on a Raspberry Pi. The tutorial is located at the URL, http://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/.

The overly simplified basis for the motion detection in this code is background subtraction using a reference frame. The code calculates the pixel differences between the current frame and the reference frame and then compares it to a threshold to determine if there is motion.

This code makes the assumption that the first frame of our video file will contain no motion and just background — therefore, we can model the background of our video stream using only the first frame of the video. As we can probably guess with a live webcam, this is probably not going to be true if we run the code sitting in front of the webcam as I did many times. Changes in lighting and shadows will also cause issues to this but this is a simple algorithm to show what could potentially be accomplished.

##Integrate I/O Functionality
The following files augment **motion_detector_statif_ref.py** by adding some IO control to the motion detector parameters
- **motion_detector_static_ref_button** - This code is an extension of **motion_detector_static_ref.py** that adds the GPIO functionality to update the reference frame based on a button press.

The following code snippet checks to see if the reference frame has been initialized as shown in the code snippet below.

```python
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
```

So we can update this reference frame by setting firstFrame to None which is what we do in the callback function shown below.

```python
# Button Callback function to create new reference frame, firstFrame
def btn_cb():
	# In order to reference the global variable, need to declare callback variable as global
	global firstFrame
	firstFrame = None
	print("Button Pressed!")
```

And finally we register the callback function, ```btn_cb``` with the GPIO as shown below

```python
btnA = Button("GPIO-A")
btnA.when_pressed(btn_cb)
```
