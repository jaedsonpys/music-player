from tkinter import *
from player import Player


class Root:
    def __init__(self, window: Tk):
        self.selected_music = None

        self.window = window
        self.player = Player()

        self.window.geometry('400x400')
        self.window.title('PyPlayer')
        self.window.resizable(0, 0)

        self.list_musics()

        Button(self.window, text='previous', command=lambda: self.player.previous_music(self.selected_music)).pack(side=LEFT)
        self.pause_button = Button(self.window, text='pause', command=self.player.pause).pack(side=LEFT)
        Button(self.window, text='next', command=lambda: self.player.next_music(self.selected_music)).pack(side=LEFT)

        self.wait_selected_music()

    def list_musics(self):
        # Label(self.window, text='Musics:').grid(row=0, column=1, pady=10, padx=10)
        
        self.musics_list = Listbox(self.window)
        self.musics = self.player.find_musics('/home/jaedsonpys/Música')

        for e, m in enumerate(self.musics):
            self.musics_list.insert(e + 1, m)

        self.musics_list.pack(side='top', expand=True, fill=BOTH, ipady=5, ipadx=5)

    def wait_selected_music(self):
        selected = self.musics_list.curselection()

        if selected:
            if selected[0] != self.selected_music:
                self.selected_music = selected[0]
                self.player.play(self.musics[selected[0]])

        self.window.after(255, self.wait_selected_music)


window = Tk()
Root(window)
window.mainloop()
