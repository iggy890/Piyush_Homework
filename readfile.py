from Songs.song import *
from Songs.songs import *

file = open("Songs/songs.csv", "r")

lines = file.readlines()

file.close()

song_s = Songs()

def list_to_song(text: str):
    song = Song()
    text = text.split(",")

    song.title = text[0]
    song.artist = text[1]
    song.year = text[2]
    if 'u' in text[3]:
        song.learnt = " not "
    elif 'l' in text[3]:
        song.learnt = " "

    return song

for i in lines:
    song_s.add_song(list_to_song(i))


song_s.display_songs()