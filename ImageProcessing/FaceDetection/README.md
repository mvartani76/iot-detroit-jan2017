#Face & Eye Detection
This repository contains information and example code on how to perform face detection using Haar Feature-based Cascade Classifiers.

##What are Cascade Classifiers?
Cascade Classifiers are a series of feature models for some sort of object image (in this case, a face or an eye). The models are separated into a series of models to improve efficiency. A majority of the time, most of the image will not be the object in question, so we start with very quick feature models that can quickly thow out regions as false. When we get to an area that is the object in question, the classifier will "cascade" or traverse through the series of feature models to determine if the object (face or eye) is detected. The object is detected if it passes through all the stages.

More information can be found in the following links:
- http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
- https://en.wikipedia.org/wiki/Cascading_classifiers

##Pre-trained classifiers
OpenCV already comes with many pre-trained classifiers for faces, eyes, smiles, objects, etc. In our examples we will use the pre-trained classifiers for the face and eyes.
- **haarcascade_frontalface_default.xml** - Cascade classifier file for faces from the front viewing angle
- **haarcascade_eye.xml** - Cascade classifier file for eyes from the front viewing angle

##Initializing Cascade Classifiers in Python Code
The Cascade Classifiers are initialized using the **CascadeClassifier** class as shown in the code snippets below.

###detect_face.py
```python
faceCascade = cv2.CascadeClassifier(XML_PATH)
```

###detect_face_eye.py
```python
faceCascade = cv2.CascadeClassifier(FACE_XML_PATH)
eyeCascade = cv2.CascadeClassifier(EYE_XML_PATH)
```

Further information on the **CascadeClassifier** class can be found at http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html.

##Detecting Objects (Faces & Eyes)
Objects are detected using the **detectMultiScale()** method as shown in the code snippets below.

###detect_face.py
```python
faces = faceCascade.detectMultiScale(
	frame,
	scaleFactor=1.2,
	minNeighbors=2,
	minSize=(50, 50),
	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
```

###detect_face_eye.py
```python
faces = faceCascade.detectMultiScale(
	frame,
	scaleFactor=1.2,
	minNeighbors=2,
	minSize=(50, 50),
	flags=cv2.cv.CV_HAAR_SCALE_IMAGE
	)
```
and

```python
eyes = eyeCascade.detectMultiScale(roi_frame)
```

Further information on the **detectMultiScale()** method can be found at
http://docs.opencv.org/2.4/modules/objdetect/doc/cascade_classification.html

##Executing the Python Program(s)
The Python Programs can be called from the command line using the following syntax.

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
