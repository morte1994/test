class Song(object):
  def sing_me(self, lyrics):
    self.lyrics = lyrics
    for line in self.lyrics:
      print line

#happy_song = Song(["asd", "dfg", "zxcv"])
#happy_song.song_me()
#join function