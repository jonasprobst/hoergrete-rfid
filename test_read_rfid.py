#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen
from num2words import num2words

reader = SimpleMFRC522()

try:
    while True:
        cardId = reader.read()
        p = Popen(["echo", "Card ID: " + str(cardId)])
        textToSpeak = num2words(cardId)
        p = Popen(["espeak", "-g180", textToSpeak, "2>/dev/null"])
finally:
    GPIO.cleanup()