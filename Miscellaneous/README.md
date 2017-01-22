#Miscellaneous Dragonboard Tips/Tricks
##Download Latest Image
For this meetup, we are going to use the latest Debian Linux build for our projects. The Debian Linux builds can be found on the 96boards website at the following URL, http://builds.96boards.org/releases/dragonboard410c/linaro/debian

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/latest_debian_image_location_96boards.png "Location of Debian Images")

The specific file that we will be using is shown here:

http://builds.96boards.org/releases/dragonboard410c/linaro/debian/latest/
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/latest_debian_image_location_96boards_filename.png "Latest Debian Image")

Please note that at this current time, SPI functionality is not enabled. The boards we will use locally will have a special image build based on this latest build that includes SPI functionality.

##Writing the Latest Image to a Micro SD Card
After downloading the specific file from the 96boards site, we can then flash the Micro SD Card using a tool such as **Win32 Disk Imager** if using a PC.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/latest_debian_image_location_96boards_flash_win32dskimager.png "Flashing Micro SD Card with Win32 Disk Imager")

##Flashing Linux onto Dragonboard 410c
<ol>
  <li>Unplug every adapter and cord from the DragonBoard 410c, then insert the microSD card that contains the version of Linux that you   desire (currently Ubuntu and Debian available)</li>
  <li>Set the S6 switch on the DragonBoard 410c to <strong>0-1-1-0</strong> (SD Boot and USB Host switches set to “ON”)</li>
  <span style="text-align:center"><img src="https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-s6-0110.png"></span>
  <li>Plug a USB mouse into either of the two USB connectors on the DragonBoard 410c</li>
  <li>Connect an HDMI monitor to the DragonBoard 410c with an HDMI cable and turn the monitor on</li>
  <li>Connect the power cable to the DragonBoard 410c</li>
  <li>When a menu appears on the screen, click on the install icon located on the top left of the window. Click YES to the prompt to           confirm that you want to flash Debian</li>
  <span style="text-align:center"><img src="https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-flash-step-6.png"></span>
  <li>When successful, a window should say “OS Installed”</li>
  <span style="text-align:center"><img src="https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-flash-step-7.png"></span>
  <li>Remove the SD card</li>
  <li>When you are ready, press OK to reboot</li>
  <span style="text-align:center"><img src="https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-flash-step-9.png"></span>
  <li>Disconnect the power cable from the DragonBoard 410c</li>
  <li>Set the S6 switches so that ONLY “USB Host” is enabled (<strong>0-0-1-0</strong>)</li>
    <span style="text-align:center"><img src="https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/dragonboard410c-s6-0010.png"></span>
  <li>Reconnect the power cable to the DragonBoard 410c which will reboot into Debian</li>
</ol>

##Set Date/Time/Timezone
There are various options/packages for configuring the time/date on a linux board. The command utility that I used for this is `timedatectl`.

###Display system date/time information
Simply run the command without and command line options to display the current time/date status
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-linux.png "Timedatectl")

###Update the system clock to a specificed date or time
Update the system clock to a specified date or time by using the `set-time` option followed by a string containing the new date/time information in the format shown below. For example, to set the time to 8:40am on January 19, 2017, I used the following command.
```
sudo timedatectl set-time "2017-01-19 08:40:00"
```
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-set-time.png "Set time")

Time is 24 hour based so to set time for PM values, use 24 hour notation as shown below...
```
sudo timedatectl set-time "2017-01-19 22:40:00"
```
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-set-time2.png "Set time PM")

###Update the system time zone
Use the `set-timezone` option followed by the time zone value to configure the time zone. To see a list of available time zones, use the flag/option `list-timezones`.

For example, here is a scrollable list of timezones produced when executing `timedatectl list-timezones`
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-listtimezones.png "Timedatectl list-timezones")

##Configure NTP-based network time synchronization
NTP, or Network Time Protocol, is a networking protocol for clock synchronization between computer systems over packet-switched, variable-latency data networks. It is intended to synchronize all participating computers to within a few milliseconds of UTC.

The timedatectl command provides a set-ntp option that controls whether NTP based network time synchronization is enabled. This option expects a boolean argument. To enable NTP-based time synchronization, run the following command:

```
timedatectl set-ntp true
```
As you could probably guess, to disable NTP-based time synchronization, run the following command:

```
timedatectl set-ntp false
```
