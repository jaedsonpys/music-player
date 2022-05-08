from typing import Union
from pygame import mixer
import os


class Player:
    def __init__(self) -> None:
        self.mixer = mixer
        self.mixer.init()
