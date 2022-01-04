#!/usr/bin/env python

# Inspired by:
# - https://pimylifeup.com/raspberry-pi-rfid-rc522/
# - https://pimylifeup.com/raspberry-pi-rfid-attendance-system/

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
  while True:
    id = reader.read()
    print("rfid_uid: ",id)
    
    # the plan:
    # if the card is a known card, play the song from the playlist
    # - get the list of cards that looks something like this: id spotify:track:0bYg9bo50gSsH3LtXe2SQn #what it is (json simpler?)
    # - compare the ids
    # - if one 
    # else append card id to the list of cards with timestamp as a comment and commit to repo (maybe read out a message or even the card id...)
    
finally:
    GPIO.cleanup()
