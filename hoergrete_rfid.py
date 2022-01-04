#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
# - https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_count.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen
from time import sleep
from num2words import num2words
from json import load

reader = SimpleMFRC522()
lastId = 0

#p = Popen(["echo", "updating cards.json from github..."])
#p = Popen(["curl", "-s", "-S", "https://raw.githubusercontent.com/jonasprobst/hoergrete-rfid/main/cards.json", ">", "cards.json"])

with open("cards.json", "r") as file:
    rfidCards = load(file)	

try:
    p = Popen(["espeak", "-ven-wm+f2", "-a15", "'ello duck, I'm ready!'", "2>/dev/null"])
    p.wait()
    while True:
        id, text = reader.read()
        if id != lastId:
            lastId = id
            if (id in rfidCards.values()):
                trackUri = rfidCards[id]['uri']
                p = Popen(["echo", "Card ID: " + str(id)])
                p = Popen(["echo", "Track URI: " + str(trackUri)])
                #p = Popen(["mpc", "stop", "-q", "&&",
                #        "mpc", "clear", "-q", "&&",
                #        "mpc", "add", str(trackUri), "&&",
                #        "mpc", "play"])
            else:
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
