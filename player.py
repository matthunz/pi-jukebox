import time
from mutagen.oggvorbis import OggVorbis
import pyglet

from arduino import Arduino

player = pyglet.media.Player()

class Audio:
    def change(source):
        song = pyglet.media.load(source, streaming=False)
        player.queue(song)

        song_info = OggVorbis(source)
        Arduino().send(song_info["title"][0])

Audio.change('music/feather.ogg')
player.play()

while True:
    print(round(player.time))
    time.sleep(1)
