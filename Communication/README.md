#Sending Messages with the Dragonboard 410c

Using Twilio, the Dragonboard410c can send both Short Message Service (SMS) and Multimedia Messaging Service (MMS) messages.

The sample code in this directory shows simple utilization of both SMS and MMS messages using Python Twilio SDK.

##Creating/Configuring a Twilio Account

In order to use the Twilio service, you must have a valid Twilio account. Twilio offers a free trial version of the account which is sufficient for the example code.

###Installing the Twilio Python SDK/Helper Library
Use the Python Package Manager, PIP, to install the library on our Dragonboard 410c.
```
pip install twilio
```
###Needed Twilio Credentials
To enable the Python code to connect to your Twilio account, we need to grab the Account SID and Auth Token from the Twilio Console shown below.

This information is then used in the following Python code to connect/authorize the client.

```python
# Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

client = TwilioRestClient(account_sid, auth_token)
```
