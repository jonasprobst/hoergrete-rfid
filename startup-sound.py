#!/usr/bin/env python

''' sartup sound

Plays a alsa sound when mopidy is fully booted
'''

from subprocess import call
from typing import SupportsRound
from requests import get
from time import sleep

try:
    while True: #wait for mopidy service
        status = call(["systemctl", "is-active", "--quiet", "mopidy"])
        if status == 0:
            break
        else:
            sleep(1)

    while True :  # if 0 (active), print "Active"
        resp = get("http://localhost:6680/iris")
        if resp.status_code < 400:
            call(["aplay", "-N", "-f", "cd", "/home/pi/hoergrete-rfid/fanfare.wav"])
            exit()
        else:
            sleep(1)
finally:
    exit()