#!/usr/bin/env python

# Alternative (seems EOF tho): https://github.com/ismailof/mopidy-json-client/blob/master/examples/demo_cli.py

from subprocess import Popen, DEVNULL
from time import sleep

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
    if not vol is None:
        p = Popen(["mpc", "volume", vol], stdout=DEVNULL).wait()
    p = Popen(["mpc", "random", str(rdm)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "single", str(sgl)], stdout=DEVNULL).wait()
    p = Popen(["mpc", "play"], stdout=DEVNULL)


play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "on")
sleep(5)
play("local:album:md5:9160794fee93e46d71064f75be07909f", "off", "off", 20)
sleep(10)
p = Popen(["mpc", "stop"], stdout=DEVNULL).wait()