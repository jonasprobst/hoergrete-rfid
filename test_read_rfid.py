#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen
from time import sleep

reader = SimpleMFRC522()
lastId = 0

try:
    while True:
        id, text  = reader.read()
        if id != lastId:
            p = Popen(["echo", "Card ID: " + str(id)])
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    GPIO.cleanup()