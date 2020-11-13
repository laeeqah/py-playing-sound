from tkinter import *
import os
from pygame import mixer
from tkinter.filedialog import askopenfilename

window = Tk()
window.geometry("700x500")
window.title("MusicPlay")
window.configure(background="grey")
mixer.init()

# Layout of tkinter
# Frame
frame1 = LabelFrame(window, text="Song Track", padx=5, pady=5)
frame1.grid(row=1, column=0)
frame1.configure(background="navy blue")

song_ent = Label(frame1, text="some songs")
song_ent.grid(row=1, column=0, padx=150)
# Frame2
frame2 = LabelFrame(window, text="Control Panel", padx=5, pady=5)
frame2.grid(row=2, column=0, padx=1, pady=1)
frame2.configure(background="grey")

# Frame3
frame3 = LabelFrame(window, text="Song Playlist", padx=5, pady=5)
frame3.grid(row=1, column=3, padx=10)
frame3.configure(background="grey")

# Scrollbar For Frame 3
track = StringVar()
song_info = StringVar()

# Functions on how to add songs
def add_music():
    window.filename = askopenfilename(filetypes=(("Wav files", "*.wav"), ("files", "*.*")))
    my_list.insert(END, window.filename)


# Button to add_Music
add_btn = Button(window, text="Add_songs", command=add_music)
add_btn.grid(row=0, column=2)

scrollbar = Scrollbar(frame3, orient="vertical")
scrollbar.grid(row=1, column=2)

my_list = Listbox(window, height = 5)
my_list.grid(row=1, column=2)
scrollbar.config(command=my_list.yview)


# my_list = ["Doja Cat - Say So (Audio).wav"]

# PLay Button and function
def play():
    mixer.music.load(my_list.get(ACTIVE))
    mixer.music.play()


play_btn = Button(frame2, text="PLAYSONG", bg="pink", fg="purple", command=play)
play_btn.grid(row=2, column=0, padx=3)


# Pause Button and function for Pause
def pause():
    song_info.set("-Paused")
    mixer.music.pause()


pause_btn = Button(frame2, text="PAUSE", bg="pink", fg="purple", command=pause)
pause_btn.grid(row=2, column=1, padx=3)


def unpause():
    song_info.set("-Playing")
    mixer.music.unpause()


unpause_btn = Button(frame2, text="UNPAUSE", bg="pink", fg="purple", command=unpause)
unpause_btn.grid(row=2, column=2, padx=3)


def stop():
    song_info.set("-Stopped")
    mixer.music.stop()


stop_btn = Button(frame2, text="STOPSONG", bg="pink", fg="purple", command=stop)
stop_btn.grid(row=2, column=3, padx=3)

window.mainloop()
