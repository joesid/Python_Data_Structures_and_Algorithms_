class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist
        self.next_song = None 



lon = Song("meat loaf", "wasted youth")

print(lon.title)
