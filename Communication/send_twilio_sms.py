#!/usr/bin/env/python

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

#Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="verified_phone_number", from_="twilio_phone_number", body="Hello There!")