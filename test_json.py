#!/usr/bin/env python

from json import load
from subprocess import Popen

print("updating cards.json")
p = Popen(["curl", "-s", "https://raw.githubusercontent.com/jonasprobst/hoergrete-rfid/main/cards.json", "-o", "cards.json"])

print("reading file")
with open("cards.json", "r") as file:
    cards = load(file)	
    print(cards)

id = 249056798748
print("check if id is known:", str(id))
if str(id) in cards:
    uri = cards[str(id)]["uri"]
    name = cards[str(id)]["name"]
    rdm = cards[str(id)]["rdm"]
    print("id found. URI: %s Name: %s rdm: %s" % (uri, name, rdm))

else:
    print("something's fishy here...")