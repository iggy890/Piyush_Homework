from Songs.song import *
from Songs.songs import *

def list_to_song(text: str):
    song = Song()
    text = text.split(",")

    song.title = text[0]
    song.artist = text[1]
    song.year = text[2]

    if 'u' in text[3]:
        song.learnt = "u"
    elif 'l' in text[3]:
        song.learnt = "l"

    return song

def encode(song: Song):
    return f"{song.title},{song.artist},{song.year},{song.learnt}\n"

def read_and_decode():
    file = open("Songs/songs.csv", "r")
    
    lines = file.readlines()

    file.close()

    song_s = Songs()

    for i in lines:
        song_s.add_song(list_to_song(i))

    return song_s

def encode_and_write(song: Song):
    f = open("Songs/songs.csv", "r")

    txt = f.read()

    f.close()

    f = open("Songs/songs.csv", "w")

    f.write(txt)
    f.write(encode(song))

    f.close()

def get_input_and_create_song():
    song = Song()
    
    song.title = input("What is the name of the song? ")
    song.artist = input("Who created the song? ")
    song.year = input("When was the song created? ")
    song.learnt = "u"

    return song
