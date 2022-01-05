#!/usr/bin/env python

from json import load
from subprocess import Popen

print("updating cards.json")
p = Popen(["curl", "-s", "https://raw.githubusercontent.com/jonasprobst/hoergrete-rfid/main/cards.json$RANDOM", "-o", "cards.json"])

print("reading file")
with open("cards.json", "r") as file:
    cards = load(file)	
    print(cards)

id = 249056798748
print("check if id is known:", str(id))
if str(id) in cards:
    trackUri = cards[str(id)]["uri"]
    trackName = cards[str(id)]["name"]
    print("id found. Track URI: ", trackUri)
    print("id found. Track URI: ", trackName)
else:
    print("something's fishy here...")