#!/usr/bin/env python

''' sartup sound

Plays a alsa sound when mopidy is fully booted
'''

from subprocess import call
from typing import SupportsRound
from requests import get
from time import sleep

try:
    print("looking for mopidy service")
    while True: #wait for mopidy service
        status = call(["systemctl", "is-active", "--quiet", "mopidy"])
        if status == 0:
            print("looking for mopidy service")
            break
        else:
            print(...)
            sleep(1)

    print("looking for iris")
    while True :  # if 0 (active), print "Active"
        resp = get("http://localhost:6680/iris")
        if resp.status_code < 400:
            call(["aplay", "-N", "-f", "cd", "/home/pi/hoergrete-rfid/fanfare.wav"])
            exit()
        else:
            print("...")
            sleep(1)
finally:
    exit()