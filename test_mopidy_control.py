#!/usr/bin/env python

# Alternative (seems EOF tho): https://github.com/ismailof/mopidy-json-client/blob/master/examples/demo_cli.py

from subprocess import Popen
from time import sleep

def play(uri, rdm):
    p = Popen(["mpc", "stop", "-q", "&&",
               "mpc", "clear", "-q", "&&",
               "mpc", "add", str(uri), "&&",
               "mpc", "random", str(rdm), "&&",
               "mpc", "play"])


play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(10)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(10)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")