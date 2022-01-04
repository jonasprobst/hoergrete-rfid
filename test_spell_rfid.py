#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen
from time import sleep
from num2words import num2words

reader = SimpleMFRC522()
lastId = 0
rfidCards = {"0":"n/a"}

try:
    p = Popen(["espeak", "-ven-wm+f2", "-a15", "'ello duck, I'm ready!'", "2>/dev/null"])
    while True:
        id, text = reader.read()
        if id != lastId:
            lastId = id
            if (id in rfidCards.values()):
                p = Popen(["echo", "Card ID: " + str(id)])
            else:
                rfidCards.update({id:"some URI"})
                textToSpeak = num2words(id)
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "sorry me duck, I've never seen this card before", "2>/dev/null"])
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "but don't you worry lovely. I'll read its id for you", "2>/dev/null"])
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "you better get a pen and paper", "2>/dev/null"])
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "well, are you ready? good!", "2>/dev/null"])
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "-g25", textToSpeak, "2>/dev/null"])
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "and remember pet, I won't fall for this twice!", "2>/dev/null"])        
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    GPIO.cleanup()
