from tkinter import *
from player import Player


class Root:
    def __init__(self, window: Tk):
        self.window = window
        self.player = Player()

        self.window.geometry('400x400')
        self.window.title('PyPlayer')
        self.window.resizable(0, 0)

        self.list_musics()

    def list_musics(self):
        # Label(self.window, text='Musics:').grid(row=0, column=1, pady=10, padx=10)
        
        self.musics_list = Listbox(self.window)
        self.musics = self.player.find_musics('/home/jaedsonpys/Música')

        for e, m in enumerate(self.musics):
            self.musics_list.insert(e + 1, m)

        self.musics_list.pack(side='top', expand=True, fill=BOTH, ipady=5, ipadx=5)


window = Tk()
Root(window)
window.mainloop()
