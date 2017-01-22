#Hands-On with the Dragonboard 410c
Repository for presentation, code, and documentation for the January 2017 IoT-Detroit Meetup about the Dragonboard 410c

##What is the Dragonboard?
The DragonBoard 410c, a product of Arrow Electronics, is the development board based on the mid-tier Qualcomm® Snapdragon™ 410E processor. It features advanced processing power, Wi-Fi, Bluetooth connectivity, and GPS, all packed into a board the size of a credit card.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-img2.jpg "Dragonboard 410c")

##Meetup Goal
During the meetup we will attempt to cover the basic features of the Dragonboard as well as the following high level concepts:
- Linker Mezzanine Card (LS Expansion Header)
- Python
- OpenCV
  - Facial Detection
  - Motion Detection
- Amazon S3
- Messaging using Twilio

We will put all these concepts together to create a smart surveillance system.

##Folder Descriptions
###AWS_s3
This folder contains information and example python code to connect to an Amazon AWS S3 bucket and upload files to the designated bucket.
###ImageProcessing
This folder contains information and example python code for facial and motion detection algorithms using OpenCV.
###Images
This folder contains the images used in the README files.
###LinkerBoard
This folder contains information and example python code for interfacing with the Linker Mezzanine Card Starter Kit.
###Messaging
This folder contains information and example python code for sending SMS/MMS messages via Twilio.
###Miscellaneous
This folder contains various tips on using the dragonboard such as connecting to WiFi or flashing linux onto the dragonboard.
###SmartSurveillance
This folder contains the code that pulls all of the concepts together to create a system that sends MMS alerts to a phone based on either motion or facial detection.

#Quick Start
##Download and Flash Debian Linux Image onto Dragonboard 410c
First we will need to make sure we are using the latest Debian Linux image. The instructions for how to do this are given in the following links below.

- [Download Latest Image](Miscellaneous/DownloadLatestImage.md)
   - Shows where the latest Dragonboard Images from 96boards.org are located and which one we are using for this project.
- [Writing Image to Micro SD Card](Miscellaneous/WriteImagetoMicroSD.md)
   - Shows how to write the downloaded Dragonboard image to a Micro SD card.
- [Flash Image onto Dragonboard 410c](Miscellaneous/FlashLinuxOntoDragonBoard.md)
   - Gives step by step instructions how to configure and flash an image onto the Dragonboard.

##Connect to WiFi
As we are going to need to download content/code from the internet, we are going to need to connect to a local wifi network as shown in the instructions [here](Miscellaneous/WiFi.md)

Grab the code used in this meetup by cloning this directory from your Dragonboard
```
git clone https://github.com/mvartani76/iot-detroit-jan2017
```
This will create a directory called **iot-detroit-jan2017**

Navigate to this directory
```
cd iot-detroit-jan2017
```
