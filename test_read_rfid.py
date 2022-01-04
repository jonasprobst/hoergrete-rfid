#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen

reader = SimpleMFRC522()

try:
    while True:
        cardId = reader.read()
        p = Popen(["echo", "Card ID: " + str(cardId)])
        
finally:
    GPIO.cleanup()