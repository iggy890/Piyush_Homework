"""
Create a class song that takes a song name, artist and release date
"""

class Song:
    def __init__(self, name: str, artist: str, date: str):
        self.song_name = name
        self.artist = artist
        self.release_date = date

class Songs:
    def __init__(self, songs: list[Song]):
        self.Songs = songs

    def add_song(self, song: Song):
        self.Songs.append(song)

    def display_songs(self):
        for i in self.Songs:
            print(f"[ {i.song_name} ]")
            
            print(f"Created by {i.artist}")
            print(f"On the {i.release_date}")

            print()

s = Song("Hello", "Adele", "17th September 2007")
s2 = Song("Long Long Long Journey", "Bill Wurtz", "29th November 2018")
songs = Songs([s, s2])
songs.display_songs()