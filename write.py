#!/usr/bin/env python

# Type some text data, then present a tag to the scanner
# to write that data to it.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()
try:
	text = input("New data: ")
	print("Now place your tag to write")
	reader.write(text)
	print("Written")
finally:
	GPIO.cleanup()


