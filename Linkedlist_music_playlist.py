class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None 


class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, title, artist):
        new_song = Song(title, artist)
        if not self.head:
            self.head = new_song
        else:
            current = self.head
            while current.next_song:
                current = current.next_song
            current.next_song = new_song

    def display_playlist(self):
        current = self.head
        while current:
            print(" \n {} by {} \n".format(current.title, current.artist))
            current = current.next_song



playlist = Playlist()

playlist.add_song("Life is a Lemon", "Meat Loaf")
playlist.add_song("Enemy", "Imagine dragons")
playlist.add_song("Enemy", "Imagine dragons")
playlist.add_song("Aerial", "System Of a Down")


playlist.display_playlist()
 