#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
# - https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_count.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen, STDOUT, DEVNULL
from time import sleep
from num2words import num2words
from json import loads
import urllib.request

reader = SimpleMFRC522()
lastId = 0

def getCards():
    print("updating cards.json from github...")
    with urllib.request.urlopen("https://raw.githubusercontent.com/jonasprobst/hoergrete-rfid/main/cards.json") as url:
        data = loads(url.read().decode())
        print(data)
    return data

# do a git pull as startup script
# or do this after every 
# p = Popen(["curl", "-s", "https://raw.githubusercontent.com/jonasprobst/hoergrete-rfid/main/cards.json", "-o", "cards.json"])
#with open("cards.json", "r") as file:
#    cards = load(file)
cards = getCards()

p = Popen(["espeak", "-ven-wm+f2", "-a15", "ello lovely, let's go!'", "2>/dev/null"], stderr=DEVNULL)
p.wait()

try:
    while True:
        id, text = reader.read()
        if id != lastId:
            lastId = id
            if (str(id) in cards):
                trackUri = cards[str(id)]["uri"]
                print("Hit play! ID: " + str(id) + " URI: " + trackUri)
                # p = Popen(["mpc", "stop", "-q", "&&",
                #        "mpc", "clear", "-q", "&&",
                #        "mpc", "add", str(trackUri), "&&",
                #        "mpc", "play"])
            else:
                # spell digits of the id rather than the number
                textToSpeak = "New I D!"
                for digit in str(id):
                    textToSpeak += num2words(int(digit)) + ", "
                p = Popen(["espeak", "-ven-wm+f2", "-a15", "-g50", textToSpeak, "2>/dev/null"], stderr=DEVNULL)
                p.wait()
                cards = getCards()
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    GPIO.cleanup()