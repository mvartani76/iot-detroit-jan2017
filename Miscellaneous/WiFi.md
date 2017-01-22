#WiFi
The Dragonboard410c has onboard single band 802.11b/g/n (WiFi) available.

##Connect to WiFi
|Steps|Screenshot Image|
|------------ |:-------------:|
|You should see the wireless network indicator in the bottom right corner | ![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linaro-wifi-indicator-toolbar.png "WiFi Indicator Toolbar")|
|Click on the wireless network indicator and select the appropriate wireless network | ![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linaro-wifi-networks.png "Available WiFi Networks")|
|Enter the network credentials (if applicable) at the prompt, and click “Connect”| ![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/linaro-wifi-authentication.png "Enter WiFi Credentials")|

##Check WiFi Status
You can check the status of the wifi connection via the command line by typing
```
sudo ifconfig
```
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/wifi_status.png "Checking WiFi Status on the Dragonboard")

Note that you will need root permissions to use this command in this image.
