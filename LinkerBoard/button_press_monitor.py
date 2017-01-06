#!/usr/bin/python

from libsoc_zero.GPIO import Button
from time import sleep

btnA = Button("GPIO-A")
btnB = Button("GPIO-B")
btnC = Button("GPIO-C")
btnD = Button("GPIO-D")
btnE = Button("GPIO-E")


while True:
	sleep(0.25)
	if btnA.is_pressed():
		print("Button A is pressed")
	elif btnB.is_pressed():
		print("Button B is pressed")
	elif btnC.is_pressed():
		print("Button C is pressed")
	elif btnD.is_pressed():
		print("Button D is pressed")
	elif btnE.is_pressed():
		print("Button E is pressed")
	else:
		print("Button not pressed")
