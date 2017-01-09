#!/usr/bin/python

from libsoc_zero.GPIO import Button
from time import sleep

def btn_cb():
	print("Button Pressed!")

def pause():
	program_pause = raw_input("")

btnA = Button("GPIO-A")

btnA.when_pressed(btn_cb)

print("Waiting for button press event...")
pause()
