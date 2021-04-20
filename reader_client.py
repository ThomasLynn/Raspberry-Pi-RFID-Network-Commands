#!/usr/bin/env python


# Takes -ip and -port arguments for the target server's ip+port.
# Waits for a tag to be presented to the rfid scanner.
# Sends the text data on the rfid to the server.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import socket
import sys
import time
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-ip", default="127.0.0.1",
    help="The ip the server should be bound to, type ipconfig (or ifconfig) in the command line to get your local ip.")
parser.add_argument("-port", default="3647", help="The port the server should be bound to.")
args = parser.parse_args()

HOST, PORT = args.ip, int(args.port)
reader = SimpleMFRC522()

try:
    # does this in a loop so you can read multiple tags
	while True:
        # reads the tag id and text
		id, text = reader.read()
		data = str(text)

		# Create a socket (SOCK_STREAM means a TCP socket)
		with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
			# Connect to server and send data
			sock.connect((HOST, PORT))
			sock.sendall(bytes(data, "utf-8"))

			# Receive data from the server, I'm too lazy to remove this
			received = str(sock.recv(1024), "utf-8")

		print("Sent:     {}".format(data))
		print("Received: {}".format(received))
        
        # sleep for a little bit so you don't read the tag multiple times really quickly
		time.sleep(0.5)
		
finally:
    # if this is not called, the next time gpio is used,
    # python will not like it
	GPIO.cleanup()

