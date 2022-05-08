from tkinter import *


class Root:
    def __init__(self, window: Tk):
        self.window = window

        self.window.geometry('400x400')
        self.window.title('PyPlayer')
        self.window.resizable(0, 0)
