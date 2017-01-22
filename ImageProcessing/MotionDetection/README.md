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
- **motion_detector_static_ref_button.py** - This code adds the GPIO functionality to update the reference frame based on a button press.
- **motion_detector_static_ref_pot.py** - This code uses the ADC/SPI interface to adjust the "min_area" parameter using the sliding potentiometer. Please note that the SPI interface is supported on the Dragonboard/Snapdragon processor while the Linker Mezzanine Card contains a Microchip 10-bit ADC that communicates to the Dragonboard via SPI. The datasheet for the MPC3004 contained in the Mezzanine Card is available here: http://ww1.microchip.com/downloads/en/DeviceDoc/21295C.pdf.

###motion_detector_static_ref_button.py
The following code snippets show the additions/modifications needed to incorporate GPIO functionality into the motion detection code.

First, we need to include the necessary libraries...
```python
from libsoc_zero.GPIO import Button
from time import sleep
```

The following code is in the initial but is just to remind the reader that the program checks to see if the reference frame has been initialized as shown in the code snippet below.

```python
	# if the first frame is None, initialize it
	if firstFrame is None:
		firstFrame = gray
		continue
```

We can update this reference frame by setting firstFrame to None which is what we do in the callback function shown below.

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
###motion_detector_static_ref_pot.py
The following code snippets show the additions/modifications needed to incorporate the ADC/SPI potentiometer into the motion detection code.

First we need to import the spidev library.
```python
import spidev
```

Next we need to configure the SPI.
```python
# configure SPI
spi = spidev.SpiDev()
spi.open(0,0)
channel_select = [0x01, 0x80, 0x00]
```

In the main loop we read in the adc data from the linker mezzanine card via SPI as shown below.
```python
# read in adc data
adc_data = spi.xfer2(channel_select)
adc = ((adc_data[1]<<8)&0x300)|(adc_data[2]&0xFF)
```

Based on a bit of empirical testing, set the min_area range to be between 200 (easy to detect motion) to 30,980 (difficult to detect motion).
```python
# min_area range is from 200 to 30,890	
min_area = round(200 + adc * 30)
```

We then modify the contourArea check to compare to ```min_area``` instead of ```args["min_area"]```, which is the command line parameter input.
```python
# if the contour is too small, ignore it
# min_area derived from potentiometer
if cv2.contourArea(c) < min_area:
	continue
```
The code above is in a loop for all countours and if the specific contour area is less than min_area, it continues to the next iteration of the loop.
##Results, Observations, and Commentary
###Calling the motion detection code
Invoking the motion detction code below
```
sudo python motion_detector_static_ref_button.py -a 5000
```
###Results
|Description|Reference Frame|Frame Delta|Thresh|Result|
|------------|:-------------:|:-------------:|:-------------:|:-------------:|
|Unoccupied|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_reference_frame_unoccupied.png "Reference Frame")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_frame_delta_unoccupied.png "Unoccupied Frame Delta")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_thresh_unoccupied.png "Unoccupied Thresh")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_live_feed_unoccupied.png "Unoccupied Result")|
|Occupied Small Contrast|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_reference_frame_unoccupied.png "Reference Frame")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_frame_delta_occupied_1.png "Small Contrast Occupied Frame Delta")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_thresh_occupied_1.png "Small Contrast Occupied Thresh")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_live_feed_occupied_1.png "Small Contrast Occupied Result")|
|Occupied Large Contrast|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_reference_frame_unoccupied.png "Reference Frame")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_frame_delta_occupied_2.png "Large Contrast Occupied Frame Delta")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_thresh_occupied_2.png "Large Contrast Occupied Thresh")|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/motion_live_feed_occupied_2.png "Large Contrast Occupied Result")|
###Observations and Commentary
The results show that the algorithm works best when there is large contrast (or differences) between current and reference frame as shown in the image where I am standing in front of a window.

When I am standing in front of the wall, there are some pixel differences but they are smaller grayscale changes compared to when I am standing in front of the window.

This algorithm also suffers from the static reference frame. As we know there will be changes in lighting conditions over time which will skew the results (shadows, etc.).
