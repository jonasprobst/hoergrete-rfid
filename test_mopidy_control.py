#!/usr/bin/env python

# Alternative (seems EOF tho): https://github.com/ismailof/mopidy-json-client/blob/master/examples/demo_cli.py

from subprocess import Popen, DEVNULL
from time import sleep

def play(uri, rdm="off", sgl="off", vol=0):
    # https://www.systutorials.com/docs/linux/man/1-mpc/
    # other pontentially useful comands: 
    # - load <file> (loads <file> as playlist)
    # - ls[<directory>] (lists all files/  folder in <directory>)
    # - single <on|off>
    # - repeat <on|off>
    # - volume [+-]<num> (set the volume to <num> odr adjust it by +/-<num>)

    p = Popen(["mpc", "stop"], stdout=DEVNULL).wait()
    p = Popen(["mpc", "clear"]).wait()
    p = Popen(["mpc", "add", str(uri)]).wait()
    if vol != 0:
        p = Popen(["mpc", "volume", vol], stdout=DEVNULL).wait()
    p = Popen(["mpc", "random", str(rdm)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "single", str(sgl)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "play"])


play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
p = Popen(["mpc", "stop"]).wait()