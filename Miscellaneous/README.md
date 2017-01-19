#Miscellaneous Dragonboard Tips/Tricks
##Configure WiFi
##Download Latest Image
##Set Date/Time/Timezone
There are various options/packages for configuring the time/date on a linux board. The command utility that I used for this is `timedatectl`.
###Display system date/time information
Simply run the command without and command line options to display the current time/date status
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-linux.png "Timedatectl")
###Update the system clock to a specificed date or time by using the `set-time` option following by a string containing the new date/time information in the format shown below. For example, to set the time to 8:40am on January 19, 2017, I used the following command.
```
sudo timedatectl set-time "2017-01-19 08:40:00"
```
###Update the system time zone
Use the `set-timezone` option followed by the time zone value to configure the time zone. To see a list of available time zones, use the flag/option `list-timezones`.

For example, here is a scrollable list of timezones produced when executing `timedatectl list-timezones`
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/timedatectl-listtimezones.png "Timedatectl list-timezones")
