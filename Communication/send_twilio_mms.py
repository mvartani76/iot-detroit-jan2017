#!/usr/bin/env/python

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
auth_token = "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy"

client = TwilioRestClient(account_sid, auth_token)

# URL where image file is located
media = "http://cs50-final.mikevartanian.me/img/dragonboard410c-img.jpg"

# Send the MMS message
message = client.messages.create(to="verified_phone_number", from_="twilio_phone_number", body="The Dragonboard is Here!", media_url=media)