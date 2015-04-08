from pygame import mixer
class MusicPlayer:
	def __init__(self, mp3file):
		mixer.init()
		mixer.music.load(mp3file)

	def play(self):
		mixer.music.play()
		while mixer.music.get_busy() == True:
			continue

if __name__ == '__main__':
	mp3player = MusicPlayer('little_love_song.mp3')
	mp3player.play()
