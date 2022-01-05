#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
# - https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_count.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen, DEVNULL
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

# TODO: 
# do a git pull as startup script instead of this more dynamic aproach?
# could use a diffrent repo and git push the new id's on there for easy editing...
cards = getCards()

# save the playout and use another way to play it to save resources?
p = Popen(["espeak", "-ven-wm+f2", "-a25", "alright! let's go!'", "2>/dev/null"], stderr=DEVNULL).wait()
#p.wait()

try:
    while True:
        id, text = reader.read()
        if id != lastId:
            lastId = id
            if (str(id) in cards):
                uri = cards[str(id)]["uri"]
                rdm = cards[str(id)]["rdm"]
                print("Hit play! ID: %s URI: %s RDM: %s" % (id, uri, rdm))
                # p = Popen(["mpc", "stop", "-q", "&&",
                #        "mpc", "clear", "-q", "&&",
                #        "mpc", "add", str(uri), "&&",
                #        "mpc", "random", str(rdm), "&&",
                #        "mpc", "play"])
                # 
                # some more options 
                # mpc random on
                # mpc volume +10  
            else:
                # spell digits of the id rather than the number
                # 
                # TODO:
                # Could save the card id in /var/lib/mopidy/rfid/ (maybe theres a way to read it if it's html or something?)
                # then only reload the json when the file exist there already

                textToSpeak = "Card ID, "
                for digit in str(id):
                    textToSpeak += num2words(int(digit)) + ", "
                p = Popen(["espeak", "-ven-wm+f2", "-a20", "-g15", textToSpeak, "2>/dev/null"], stderr=DEVNULL)
                p.wait()
                cards = getCards()
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    p = Popen(["mpc", "stop"])
    GPIO.cleanup()
