#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen
from time import sleep
from num2words import num2words

reader = SimpleMFRC522()
lastId = 0

try:
    p = Popen(["espeak", "-ven-wm+f2", "-a15", "'ello duck, I'm ready!'", "2>/dev/null"])
    while True:
        id, text  = reader.read()
        if id != lastId:
            p = Popen(["echo", "Card ID: " + str(id)])
            lastId = id
        else:
            textToSpeak = num2words(cardId)
            p = Popen(["espeak", "-ven-wm+f2", "-a15", "sorry me duck, I've never seen this card before", "2>/dev/null"])
            p = Popen(["espeak", "-ven-wm+f2", "-a15", "but don't you worry lovely. I'll read its id for you", "2>/dev/null"])
            p = Popen(["espeak", "-ven-wm+f2", "-a15", "you better get a pen and paper", "2>/dev/null"])
            p = Popen(["espeak", "-ven-wm+f2", "-a15", "are you ready? good!", "2>/dev/null"])
            p = Popen(["espeak", "-ven-wm+f2", "-a15", "-g25", textToSpeak, "2>/dev/null"])
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    GPIO.cleanup()