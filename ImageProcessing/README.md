#Image Processing using OpenCV

The following examples illustrate some image processing techniques using Python OpenCV.

The default linaro debian image that we are using for these examples did not come with Python OpenCV so we need to install it as shown below.

```
sudo apt-get install python-opencv
```
As of the time of this exercise, the above command installed Python OpenCV 2.4.9.1 as shown below.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/python-opencv-install-jan2017.png "Python OpenCV Install")
##Example Code
The following folders contain various image processing aspects
- FaceDetection - This folder contains face and eye detection code using Cascade Classifiers
- MotionDetection - This folder contains a variety of motion detection algorithms
##Various OpenCV functions
###Capturing Video from File or Device
The function prototype from the OpenCV 2.4.9 Documentation located at http://docs.opencv.org/2.4.9/modules/highgui/doc/reading_and_writing_images_and_video.html#videocapture is shown here
```
cv2.VideoCapture(filename) → <VideoCapture object>
cv2.VideoCapture(device) → <VideoCapture object>
```
We use the latter option in our examples...
```
camera = cv2.VideoCapture(0)
```
###Displaying Video/Image
The function prototype from the OpenCV 2.4.9 Documentation located at http://docs.opencv.org/2.4.9/modules/highgui/doc/user_interface.html?highlight=imshow#imshow is shown here
```
cv2.imshow(winname, mat) → None
```
with the following parameters:
```
Parameters:	
winname – Name of the window.
image – Image to be shown.
```
An example of this function used in the motion detector code is shown below...
```
cv2.imshow("Security Feed", frame)
```
###Convert Image from One Color Space to Another
The function prototype from the OpenCV 2.4.9 Documentation located at http://docs.opencv.org/2.4.9/modules/imgproc/doc/miscellaneous_transformations.html#cvtcolor is shown here
```
cv2.cvtColor(src, code[, dst[, dstCn]]) → dst
```
with the following parameters:
```
Parameters:	
src – input image: 8-bit unsigned, 16-bit unsigned ( CV_16UC... ), or single-precision floating-point.
dst – output image of the same size and depth as src.
code – color space conversion code (see the description below).
dstCn – number of channels in the destination image; if the parameter is 0, the number of the channels is derived automatically from src and code .
```
In order to reduce computational complexity and potentially improve performance, many image processing algorithms convert the images to grayscale.

This is done in the motion detection code as shown below...
```
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
```
###Thresholding Images
The function prototype from the OpenCV 2.4.9 Documentation located at http://docs.opencv.org/2.4.9/modules/imgproc/doc/miscellaneous_transformations.html#threshold is shown here
```
cv2.threshold(src, thresh, maxval, type[, dst]) → retval, dst
```
with the following parameters:
```
Parameters:	
src – input array (single-channel, 8-bit or 32-bit floating point).
dst – output array of the same size and type as src.
thresh – threshold value.
maxval – maximum value to use with the THRESH_BINARY and THRESH_BINARY_INV thresholding types.
type – thresholding type (see the details below).
```
Below is an example of how the threshold function is used in the motion detection code
```
thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
```
This example sets pixel values less than 25 to 0 and above 25 to 255.
