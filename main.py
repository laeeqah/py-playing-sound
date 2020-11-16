from tkinter import *
from pygame import mixer
import pygame
from tkinter.filedialog import askopenfilename

window = Tk()
window.geometry("850x500")
window.title("MusicPlay")
window.configure(background="grey")
pygame.mixer.init()

# Layout of tkinter

# Frame1
frame1 = LabelFrame(window, text="Song Track", padx=5, pady=5)
frame1.grid(row=0, column=0)
frame1.configure(background="navy blue")

song_ent = Label(frame1, text="Song Info", width = 50, bg = "navy blue", fg = "yellow")
song_ent.grid(row=0, column=0, padx=10)

# Frame2
frame2 = LabelFrame(window, text="Control Panel", padx=5, pady=5)
frame2.grid(row=1, column=0, padx=10)
frame2.configure(background="grey")

# Frame3
frame3 = LabelFrame(window, text="Song Playlist", padx=5, pady=5)
frame3.grid(row=1, column=2, padx=10)
frame3.configure(background="grey")

# Functions Frame 3
track = StringVar()
song_info = StringVar()

# Functions on how to add songs
def add_music():

    window.filename = askopenfilename(filetypes=(("Wav files", "*.wav"), ("files", "*.*")))
    my_list.insert(END, window.filename[45::1])

# Button to add_Music
add_btn = Button(window, text="Add_songs", command=add_music)
add_btn.grid(row=0, column=2)

scrollbar = Scrollbar(frame3, orient = VERTICAL)
scrollbar.grid(row = 1,column = 3)

my_list = Listbox(frame3, height = 5, width = 40,fg = "navy blue", selectbackground = "yellow", yscrollcommand = scrollbar.set)
my_list.grid(row=1, column=2)
my_list.config(background = "grey")
scrollbar.config(command = my_list.yview)

# Play Button and function
def play():
    print(my_list.get(ACTIVE))
    name = my_list.get(ACTIVE)
    x = name[50::-1]
    y = x[::-1]
    mixer.music.load("/home/user/Documents/py-play-sound-ex1/songs/"+my_list.get(ACTIVE))
    mixer.music.play()
    song_ent.config(text=y + " -Playing")


play_btn = Button(frame2, text="PLAYSONG", bg="pink", fg="purple", command=play)
play_btn.grid(row=3, column=0)


# Pause Button and function
def pause():
    name = my_list.get(ACTIVE)
    x = name[50::-1]
    y = x[::-1]
    mixer.music.pause()
    song_ent.config(text=y + " -Paused")


pause_btn = Button(frame2, text="PAUSE", bg="pink", fg="purple", command=pause)
pause_btn.grid(row=3, column=1, padx=3)


# Unpause Button and function
def unpause():
    name = my_list.get(ACTIVE)
    x = name[50::-1]
    y = x[::-1]
    mixer.music.unpause()
    song_ent.config(text=y + " -Unpause")


unpause_btn = Button(frame2, text="UNPAUSE", bg="pink", fg="purple", command=unpause)
unpause_btn.grid(row=3, column=2, padx=3)

# Stop Button and function
def stop():
    name = my_list.get(ACTIVE)
    x = name[50::-1]
    y = x[::-1]
    mixer.music.stop()
    song_ent.config(text=y + " -Stopped")


stop_btn = Button(frame2, text="STOPSONG", bg="pink", fg="purple", command=stop)
stop_btn.grid(row=3, column=3, padx=3)

window.mainloop()
