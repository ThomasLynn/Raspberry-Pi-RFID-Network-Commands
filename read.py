#!/usr/bin/env python

# Waits for a tag to be presented to the scanner,
# then prints the tag id and tag text to the screen.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
	id, text = reader.read()
	print("id",id)
	print("text",text)
finally:
	GPIO.cleanup()
