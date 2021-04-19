#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import socket
import sys
import time

HOST, PORT = "192.168.1.77", 3647
reader = SimpleMFRC522()

try:
	while True:
		id, text = reader.read()
		data = str(text)

		# Create a socket (SOCK_STREAM means a TCP socket)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			# Connect to server and send data
			sock.connect((HOST, PORT))
			sock.sendall(bytes(data, "utf-8"))

			# Receive data from the server and shut down
			received = str(sock.recv(1024), "utf-8")

		print("Sent:     {}".format(data))
		print("Received: {}".format(received))
		time.sleep(0.5)
		
finally:
	GPIO.cleanup()

