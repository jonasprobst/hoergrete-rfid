#!/usr/bin/env python

# https://github.com/ismailof/mopidy-json-client/blob/master/examples/demo_cli.py

from mopidy-json-client import MopidyClient

mopidy = MopidyClient()

mopidy.tracklist.clear()
mopidy.tracklist.add("spotify:track:4ZiMMIaoK9sSI1iQIvHSq8")
mopidy.playback.play()


#'test': ['spotify:track:4ZiMMIaoK9sSI1iQIvHSq8',
#                            'tunein:station:s24989',
#                            'podcast+http://feeds.feedburner.com/aokishouse#http://traffic.libsyn.com/steveaoki/037_AOKIS_HOUSE_-_STEVE_AOKI.mp3',
#                            'bt:stream',
#                            ],