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
    p.wait()
    while True:
        id, text = reader.read()
        if id != lastId:
            lastId = id
            if (id in rfidCards.values()):
                p = Popen(["echo", "Card ID: " + str(id)])
            else:
                rfidCards.update({id:"some URI"})
                # spell digits of the id rather than the number
                textToSpeak = ""
                for digit in str(id):
                    textToSpeak += num2words(int(digit)) + ", "
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "sorry me duck, I've never seen this ID before", "2>/dev/null"])
                p.wait()
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "-g25", textToSpeak, "2>/dev/null"])
                p.wait()      
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    GPIO.cleanup()
