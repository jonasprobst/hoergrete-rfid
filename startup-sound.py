#!/usr/bin/env python

''' sartup sound

Plays a alsa sound when mopidy is fully booted
'''

from subprocess import call
from typing import SupportsRound
from requests import get
from time import sleep
from timeit import default_timer as timer

try:
    start = timer()
    print("looking for mopidy service")
    while True: #wait for mopidy service
        status = call(["systemctl", "is-active", "--quiet", "mopidy"])
        if status == 0:
            print("mopidy found!")
            break
        else:
            print("...")
            sleep(1)

    print("looking for iris")
    while True :  # if 0 (active), print "Active"
        try:
            resp = get("http://localhost:6680/iris")
            if resp.status_code < 400:
                call(["aplay", "-N", "-f", "cd", "/home/pi/hoergrete-rfid/fanfare.wav"])
                stop = timer()
                print("this took: ")
                print(stop - start)
                exit()
            else:
                print("something's fishy - might even be my code :-S")
                exit()
        except Exception as e:
            print(e)
            print("let's keep trying...")
            sleep(5)
except Exception as e:
    print(e)
finally:    
    exit()
