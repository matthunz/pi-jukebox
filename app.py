import os
from flask import Flask, render_template, request

from audio import Audio

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "GET":
        songs = []
        for song in os.listdir('music'):
            songs.append(os.path.splitext(song)[0])
        return render_template('index.html', songs=songs)

@app.route('/change', methods=["POST"])
def change():
    Audio.change('music/' + request.json['song'] + '.ogg')
    Audio.play()

    return 'Track changed'


app.run(debug=True)
