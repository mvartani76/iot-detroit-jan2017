#!/usr/bin/env/python

# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

#Find these values at https://twilio.com/user/account
account_sid = "AC87537ff7f21516ec81a5c2b64fedbce9"
auth_token = "66dc2528dd3bf553095c225ad60c0cb8"

client = TwilioRestClient(account_sid, auth_token)

media = "http://cs50-final.mikevartanian.me/img/dragonboard410c-img.jpg"

message = client.messages.create(to="+12482144561", from_="+12486394814", body="The Dragonboard is Here!", media_url=media)