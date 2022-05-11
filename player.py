from typing import Union
from pygame import mixer
import os


class Player:
    def __init__(self) -> None:
        self.mixer = mixer
        self.mixer.init()

        self.musics = []
        self.is_paused = False

    def find_musics(self, dirpath: str) -> list:
        def filter_music_files(filename: str) -> Union[str, None]:
            if filename.endswith('.mp3'):
                return os.path.join(dirpath, filename)

        if os.path.isdir(dirpath):
            files: list = os.listdir(dirpath)
            self.musics = list(map(filter_music_files, files))

            return self.musics

    def play(self, filepath: str):
        self.mixer.music.load(filepath)
        self.mixer.music.play()

    def previous_music(self, last_music_index: int):
        try:
            next_music = self.musics[last_music_index - 1]
        except IndexError:
            return None
        else:
            self.play(next_music)

    def next_music(self, last_music_index: int):
        try:
            next_music = self.musics[last_music_index + 1]
        except IndexError:
            return None
        else:
            self.play(next_music)

    def pause(self):
        if self.is_paused:
            self.unpause()
            self.is_paused = False
        else:
            self.mixer.music.pause()
            self.is_paused = True

    def unpause(self):
        self.mixer.music.unpause()
