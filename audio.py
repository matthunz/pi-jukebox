import time
from mutagen.oggvorbis import OggVorbis
import pyglet

from arduino import Arduino

player = pyglet.media.Player()

class Audio:
    def change(source):
        song = pyglet.media.load(source)
        player.queue(song)

        if player.playing:
            player.next_source()

        song_info = OggVorbis(source)
        Arduino().display(song_info["title"][0])

    def play():
        player.play()
