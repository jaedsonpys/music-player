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
                return filename

        if os.path.isdir(dirpath):
            musics: list = os.listdir(dirpath)
            filter(filter_music, musics)
