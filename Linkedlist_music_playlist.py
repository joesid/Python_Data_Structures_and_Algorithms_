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
 