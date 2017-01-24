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

##Git the code
Grab the code used in this meetup by cloning this directory from your Dragonboard
```
git clone https://github.com/mvartani76/iot-detroit-jan2017.git
```
This will create a directory called **iot-detroit-jan2017**

Navigate to this directory
```
cd iot-detroit-jan2017
```
We are now ready to begin looking through the code and configuring our setup to run the various examples.

##Using the Linker Mezzanine Card
We will first look at interacting with some of the peripherals of the board using the Linker Mezzanine Card Starter Kit as shown [here](LinkerBoard/README.md)
##Image Processing
Next we will explore some Image Processing concepts [here](ImageProcessing/README.md)
##Using Twilio
Then we will set up a Twilio account to send SMS/MMS messages [here](Messaging/README.md)
##AWS S3
As we observed some of the requirements of sending MMS messages, we will learn to set up and configure an S3 bucket and interface via Python [here](AWS_s3/README.md)
##Smart Surveillance
We then put it all together and create a simple smart surveillance system using the concepts we previously learned [here](SmartSurveillance/README.md)
