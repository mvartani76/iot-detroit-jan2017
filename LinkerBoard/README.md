#LinkerBoard Code

The following directory contains code snippets that demonstrate some of the functionality of the linker mezzanine card.

##Linker Mezzanine Card
The Linker Mezzanine Card is a shield for 96boards compatible devices such as the Dragonboard 410c.
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linker_mezzanine_card_photo1.jpg "Linker Mezzanine Card")

###Testing Touch Sensor and Sliding Potentiometer
The included code in this directory will test the functionality of the Touch Sensor and Sliding Potentiometer.

####Touch Sensor
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linker-touch-sensor.jpg "Linker Touch Sensor")

`button_press_monitor.py` and `wait_for_button_press.py` utilize/test the touch sensor module with the former code using a polling loop and the latter using interrupts/callback functions.

The code requires that the touch sensor module is plugged into the header labeled **D1**.

####Sliding Potentiometer
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linker-sliding-potentiometer.jpg "Linker Sliding Potentiometer")

`spi_monitor.py` uses a polling loop to read data from the sliding potentiometer via the ADC.

The code requires that the sliding potentiometer module is plugged into the header labeled **ADC1**.

##Installing libsoc library

Some of the code that utilizes GPIOs/ADCs/SPI/I2C/etc. requires the use of the libsoc library.

This library and documentation is located here: https://github.com/jackmitch/libsoc

Before we try to make the library, we need to make sure that we have all of the necessary prequisite packages...

```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install autoconf
sudo apt-get install automake
sudo apt-get install libtool
sudo apt-get install libtool-bin
sudo apt-get install python-dev
```

Grab the libsoc code from Github...
```
git clone https://github.com/jackmitch/libsoc
```
cd libsoc

Configure/install the libsoc build scripts using autoreconf

```
autoreconf -i
```

Configure the library to use the dragonboard410c board python 2.7 bindings
```
./configure --enable-board=dragonboard410c --enable-python=2
```

Connect the libs to the source and create the required links and sets it up for the final phase it also parses the human readable to machine readable using the "make" command

```
make
```

Create the binary files and move all required files / executables and associated libs to their appropriate directories. This is done as root.

```
sudo make install
```

Map the shared library name (libsoc) to the location of the corresponding shared library file (/usr/local/lib).
```
sudo ldconfig
```

This code utilizes the libsoc_zero library to remove some of the code and simplify things a bit. Type the following commands to install the library using the Python Package Manager, PIP
```
sudo apt-get install python-pip
pip install libsoc_zero
```
##Enabling SPI
In order to use the included sliding potentiometer, we need to enable SPI functionality. Unfortunately this is a complicated process that involves rebuilding the linux kernel as shown in the following URL, https://github.com/96boards/documentation/blob/master/ConsumerEdition/DragonBoard-410c/Configuration/EnableSPI.md.

As a simple work around, an SD card image with SPI enabled is included in the SDCard_Images directory. Please note that this is just a temporary work around and may go out of date quickly so always check http://builds.96boards.org/releases/dragonboard410c/ for the latest build images.

Okay so now that we have that out of the way, we enable SPI functionality by executing the following code
```
pip install spidev
```
##Code Examples
###button_press_monitor.py
This code just sets up an infinite loop and checks to see if a button is pressed as shown in the snippet below.
```python
while True:
	sleep(0.25)
	if btnA.is_pressed():
		print("Button A is pressed")
```
The code is run by typing the following...
```
sudo python button_press_monitor.py
```
The code output is shown below...
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linkerboard_button_press_monitor.png "button_press_monitor.py results")
###wait_for_button_press.py
This code has the same purpose as above but uses interrupts/callback functions for interacting with the button press. The following code snippet shows the callback function, initiating the ```when_pressed()```, and the conditional exit based on keyboard interrupt.
```python
def btn_cb():
	print("Button Pressed!")

def pause():
	program_pause = raw_input("")

btnA = Button("GPIO-A")

btnA.when_pressed(btn_cb)

print("Waiting for button press event...")
try:
	pause()
except KeyboardInterrupt:
	print("Program Closed")
	btnA.close()
	pass
```
The code is run by typing the following...
```
sudo python wait_for_button_press.py
```
The code output is shown below...
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linkerboard_waitforbuttonpress.png "wait_for_button_press.py results")
###spi_monitor.py
This code utilizes the dragonboard SPI to interface with the ADC on the linkerboard mezzanine card. The following code snippet shows the configuration of the SPI and the infinite loop that reads/formats the data from the ADC/SPI...
```python
spi = spidev.SpiDev()
spi.open(0,0)
channel_select = [0x01, 0x80, 0x00]

while True:
	adc_data = spi.xfer2(channel_select)
	adc = ((adc_data[1]<<8)&0x300)|(adc_data[2]&0xFF)
	print(round((adc / 1023.0) * 100))
	sleep(0.5)
```
Note that the ADC is a 10 bit ADC and therefore the maximum number is 1023.
The code output is shown below...
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linkerboard_spimonitor.png "spi_monitor.py results")
