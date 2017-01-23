#Sending Messages with the Dragonboard 410c

Using Twilio, the Dragonboard410c can send both Short Message Service (SMS) and Multimedia Messaging Service (MMS) messages.

The sample code in this directory shows simple utilization of both SMS and MMS messages using Python Twilio SDK.

##Creating/Configuring a Twilio Account

In order to use the Twilio service, you must have a valid Twilio account. Twilio offers a free trial version of the account which is sufficient for the example code.

###Creating Twilio Account
If you do not already have a Twilio account, please navigate to https://www.twilio.com/try-twilio and create a free account.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/create-twilio-account.jpg "Twilio Sign Up Page")

###Installing the Twilio Python SDK/Helper Library
Use the Python Package Manager, PIP, to install the library on our Dragonboard 410c.
```
pip install twilio
```
![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/pip-install-twilio.png "pip install twilio")
###Needed Twilio Credentials
To enable the Python code to connect to your Twilio account, we need to grab the **Account SID** and **Auth Token** from the Twilio Console shown below.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/twilio_console_needed_account_details.jpg "Twilio Account Details")

This information is then used in the following Python code to connect/authorize the client.

```python
# Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

client = TwilioRestClient(account_sid, auth_token)
```
### Twilio Phone Number Activation
To send the messages, you will need to create/choose a Twilio phone number.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/twilio-phone-number_crop.jpg "Twilio Phone Number Activation")

Please make sure that the phone number has both SMS and MMS capabilities in order to successfully run the example code.

![alt text](https://github.com/mvartani76/iot-detroit-jan2017/blob/master/Images/twilio-phone-number-capabilities.jpg "Twilio Phone Number Capabilities")

The following two code snippets show where the Twilio Phone Number is used...

**send_twilio_sms.py**
```python
# Send the SMS message
message = client.messages.create(to="verified_phone_number", from_="twilio_phone_number", body="A message from your Dragonboard 410c!")
send_twilio_mms.py
```
**send_twilio_mms.py**
```python
# Send the MMS message
message = client.messages.create(to="verified_phone_number", from_="twilio_phone_number", body="The Dragonboard is Here!", media_url=media)
```
