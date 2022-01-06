#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/
# - https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_count.py

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from subprocess import Popen, DEVNULL
from time import sleep
from json import loads
import urllib.request

def play(uri, rdm="off", sgl="off", vol=None):
    # https://www.systutorials.com/docs/linux/man/1-mpc/
    # other pontentially useful comands:
    # - load <file> (loads <file> as playlist)
    # - ls[<directory>] (lists all files/  folder in <directory>)
    # - single <on|off>
    # - repeat <on|off>
    # - volume [+-]<num> (set the volume to <num> odr adjust it by +/-<num>)

    p = Popen(["mpc", "stop"], stdout=DEVNULL).wait()
    p = Popen(["mpc", "clear"], stdout=DEVNULL).wait()
    p = Popen(["mpc", "add", str(uri)], stdout=DEVNULL).wait()
    if vol is not None:
        p = Popen(["mpc", "volume", str(vol)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "random", str(rdm)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "single", str(sgl)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "play"])


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

reader = SimpleMFRC522()

# create and clean the dir new card id's are saved to (you can brows them in iris)
p = Popen(["sudo", "mkdir", "-p", "/var/lib/mopidy/rfid"]).wait()
p = Popen(["sudo", "rm", "-r", "/var/lib/mopidy/rfid/*"])

# save the playout and use another way to play it to save resources?
p = Popen(["espeak", "-ven-wm+f2", "-a25", "alright! let's go!'", "2>/dev/null"], stderr=DEVNULL)

try:
    while True:
        id, text = reader.read()
        if (str(id) in cards):
            uri = cards[str(id)]["uri"]
            rdm = cards[str(id)]["rdm"]
            sgl = cards[str(id)]["sgl"]
            play(uri, rdm, sgl)
        else:
            # write a file with the id as name to mopidy so it can be viewed in iris
            # TODO: only reload the json when the file exists already (save some resources, maybe?)
            p = Popen(["sudo", "touch", "/var/lib/mopidy/rfid/"+str(id)])
            cards = getCards()
        sleep(5)
except KeyboardInterrupt:
    raise
finally:
    p = Popen(["mpc", "stop"])
    GPIO.cleanup()
