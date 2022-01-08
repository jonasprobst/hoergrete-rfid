#!/usr/bin/env python

''' sartup sound

Plays a sound when mopidy is fully booted.
This script will give up after 5min.
(I know it's a nasty bit of code :-S)

To run this on boot:
* sudo nano /etc/rc.local
* add the following line before "EXIT":
    * sudo python3 /home/pi/hoergrete-rfid/startup-sound.py &
* make script executable: sudo chmod +x /etc/rc.local
* reboot and hope for the best

'''

from subprocess import call
from requests import get
from time import sleep
from timeit import default_timer as timer

start = timer()

def sleepOrExit(naptime=1):
    lap = timer()
    if lap - start >= 300:
        # time is up: play game over sound and abandone ship.
        call(["aplay", "-N", "-f", "cd", "/home/pi/hoergrete-rfid/gameover.wav"])
        exit()
    else:
        sleep(naptime)
        return

try:
    # wait for mopidy service
    while True: #wait for mopidy service
        status = call(["systemctl", "is-active", "--quiet", "mopidy"])
        if status == 0:
            break
        else:
            sleepOrExit(1)

    # Wait for iris webui
    while True : 
        try:
            resp = get("http://localhost:6680/iris")
            if resp.status_code < 400:
                call(["aplay", "-N", "-f", "cd", "/home/pi/hoergrete-rfid/fanfare.wav"])
                break
            else:
                print("Error: iris is running but returned status code: ", resp.status_code)
                exit()
        except Exception as e:
                # Iris isn't running yet, let's keep trying...
                sleepOrExit(5)

except Exception as e:
    print(e)
finally:    
    exit()
