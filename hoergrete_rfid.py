#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
# - https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_count.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from num2words import num2words
import json
from subprocess import Popen

reader = SimpleMFRC522()

p = Popen(["echo", "updating cards.json from github..."])
p = Popen(["curl", "-s", "-S", "https://raw.githubusercontent.com/jonasprobst/hoergret_rfid/master/cards.json", ">", "cards.json"])

with open("/path/to/file", "r") as file:
    rfidCards = json.load(file)	

try:
    while True:
        # wait for a card to be scanned
        cardId = reader.read()
        p = Popen(["echo", "Scanned a card: " + str(cardId)])
        if (cardId in rfidCards.values()):
            # this is a known card id. hit play it on mopidy
            # print("Known card: "+cardId+" - hit play on: "+trackUri)
            trackUri = rfidCards[cardId]['uri']
            p = Popen(["echo", "Known card. hit play on track " + str(trackUri)])
            p = Popen(["mpc", "stop", "-q", "&&",
                       "mpc", "clear", "-q", "&&",
                       "mpc", "add", str(trackUri), "&&",
                       "mpc", "play"])
        else:
            # this is an unknown card id. read it out loud
            # write it down and add it to the cards list on github
            # the list will be synced on every startup
            #print("Unknown card: "+cardId+" - read it out loud...")
            p = Popen(["echo", "Unknown card. Read out the card id"])
            textToSpeak = num2words(cardId)
            p = Popen(
                ["espeak", "sorry, i do not know this card", "2>/dev/null"])
            p = Popen(["espeak", "-g180", textToSpeak, "2>/dev/null"])
finally:
    GPIO.cleanup()
