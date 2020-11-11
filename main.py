from tkinter import *
import pygame
import os
from pygame import mixer


window = Tk()
window.geometry("700x500")
window.title("MusicPlay")
window.configure(background = "grey")


# Layout of tkinter
#Frame
frame = LabelFrame(window, text = "Song Track", padx = 5, pady = 5)
frame.grid(row = 0, column = 0)
frame.configure(background ="navy blue")

#Frame2
frame2 = LabelFrame(window, text = "Control Panel", padx = 5, pady = 5)
frame2.grid(row = 1, column = 0, padx = 1, pady = 1)
frame2.configure(background ="grey")

#Frame3
frame3 = LabelFrame(window, text = "Song Playlist",padx = 5, pady = 5)
frame3.grid(row = 0, column = 1)
frame3.configure(background = "grey")

#Scrollbar For Frame 3
track = StringVar()
song_info = StringVar()

pygame.init()
pygame.mixer.init()

scrollbar = Scrollbar(frame3, orient = "vertical")
scrollbar.grid(row = 0, column = 3)
my_list = Listbox(frame3, width = 20, height = 5, yscrollcommand=scrollbar.set,selectbackground="gold",selectmode=SINGLE,
                  font=("times new roman",12,"bold"),bg="silver",fg="navyblue",bd=5,relief=GROOVE)
my_list.grid(row = 0, column = 2)
scrollbar.config(command = my_list.yview)
my_list = ["Doja Cat - Say So (Audio).wav"]

# os.chdir("songs")
# songtracks = os.listdir()
# for track in songtracks:
#       my_list.insert(END,track)

#Buttons to frame2
def play():
    pygame.mixer.music.load("songs/Doja Cat - Say So (Audio) (online-audio-converter.com).wav")
    pygame.mixer.music.play()

play_btn = Button(frame2, text = "PLAYSONG", bg = "pink",fg = "purple", command = play)
play_btn.grid(row = 1, column = 0, padx = 3)

def pause():
    song_info.set("-Paused")
    pygame.mixer.music.pause()

pause_btn = Button(frame2, text = "PAUSE", bg = "pink", fg = "purple", command = pause)
pause_btn.grid(row = 1, column = 1, padx = 3)

def unpause():
    song_info.set("-Playing")
    pygame.mixer.music.unpause()
unpause_btn = Button(frame2, text = "INPAUSE", bg = "pink", fg = "purple",command= unpause)
unpause_btn.grid(row = 1, column = 2, padx = 3)

def stop():
    song_info.set("-Stopped")
    pygame.mixer.music.stop()

stop_btn = Button(frame2, text = "STOPSONG", bg = "pink",fg = "purple" ,command = stop)
stop_btn.grid(row = 1, column = 3, padx = 3)


window.mainloop()


