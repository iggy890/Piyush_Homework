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

            if i.learnt == "l\n":
                print("Song has been learnt")
            elif i.learnt == "u\n":
                print("Song has not been learnt")

            print()
