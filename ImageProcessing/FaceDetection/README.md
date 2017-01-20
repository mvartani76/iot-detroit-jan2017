#Face & Eye Detection
This repository contains information and example code on how to perform face detection using Haar Feature-based Cascade Classifiers.

##Pre-trained classifiers
OpenCV already comes with many pre-trained classifiers for faces, eyes, smiles, objects, etc. In our examples we will use the pre-trained classifiers for the face and eyes.
- **haarcascade_frontalface_default.xml** - Cascade classifier file for faces from the front viewing angle
- **haarcascade_eye.xml** - Cascade classifier file for eyes from the front viewing angle

##Calling the function(s)
The two functions can be called from the command line using the following syntax.

###detect_face.py
```
python detect_face.py haarcascade_frontalface_default.xml
```
###detect_face_eye.py
```
python detect_face_eye.py haarcascade_frontalface_default.xml haarcascade_eye.xml
```

Note that the cascade files are passed into the python function(s) as arguments and are read from the following lines of python code shown below.

**detect_face.py** using just one parameter input
```python
# Get XML file input
if len(sys.argv) > 1:
	XML_PATH = sys.argv[1]
else:
	print "Error: XML path not defined"
	sys.exit(1)
  ```
  
  **detect_face_eye.py** using two parameter inputs
  ```python
  # Get XML file input
if len(sys.argv) > 1:
	FACE_XML_PATH = sys.argv[1]
	EYE_XML_PATH = sys.argv[2]
else:
	print "Error: XML path not defined"
	sys.exit(1)
  ```
##Results
|detect_face.py|detect_face_eye.py|
|:------------:|:-------------:|
|![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/face_detect_result.png "Face Detection Result")| ![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/face_detect_eye_result.png "Face & Eye Detection Result")|
