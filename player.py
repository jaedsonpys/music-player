from typing import Union
from pygame import mixer
import os


class Player:
    def __init__(self) -> None:
        self.mixer = mixer
        self.mixer.init()

    def find_musics(self, dirpath: str) -> list:
        def filter_music(filename: str) -> Union[str, None]:
            if filename.endswith('.mp3') or filename.endswith('.mp4a'):
                return os.path.join(dirpath, filename)

        if os.path.isdir(dirpath):
            musics: list = os.listdir(dirpath)
            musics = list(filter(filter_music, musics))

            return musics

    def play(self, filepath: str):
        self.mixer.music.load(filepath)
        self.mixer.music.play()

    def pause(self):
        self.mixer.music.pause()

    def unpause(self):
        self.mixer.music.unpause()
