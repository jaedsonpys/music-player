from typing import Union
from pygame import mixer
import os


class Player:
    def __init__(self) -> None:
        self.mixer = mixer
        self.mixer.init()

        self.musics = []

    def find_musics(self, dirpath: str) -> list:
        def filter_music_files(filename: str) -> Union[str, None]:
            if filename.endswith('.mp3') or filename.endswith('.mp4a'):
                return os.path.join(dirpath, filename)

        if os.path.isdir(dirpath):
            files: list = os.listdir(dirpath)
            self.musics = list(map(filter_music_files, files))

            return self.musics

    def play(self, filepath: str):
        self.mixer.music.load(filepath)
        self.mixer.music.play()

    def pause(self):
        self.mixer.music.pause()

    def unpause(self):
        self.mixer.music.unpause()
