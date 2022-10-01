class Songs:
    def __init__(self, songs: list = []):
        self.Songs = songs

    def add_song(self, song):
        self.Songs.append(song)

    def display_songs(self):
        for i in self.Songs:
            print(f"[ {i.title} ]")

            print(f"Created by {i.artist}")
            print(f"Created in {i.year}")

            print(f"Song has{i.learnt}been learnt")

            print()
