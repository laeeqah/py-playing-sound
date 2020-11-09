from tkinter import *
from tkinter import ttk
from playsound import playsound


window = Tk()
window.geometry("700x500")
window.title("MusicPlay")
window.configure(background = "grey")
# Layout of tkinter
#Frame
frame = LabelFrame(window, text = "Song Track", padx = 5, pady = 5)
frame.grid(row = 0, column = 0)
frame.configure(background ="navy blue")

label = Label(frame, text = "name of songs")
label.grid(row = 0, column = 0, padx = 140)

#Frame2
frame2 = LabelFrame(window, text = "Control Panel", padx = 5, pady = 5)
frame2.grid(row = 1, column = 0, padx = 1, pady = 1)
frame2.configure(background ="grey")

#Frame3
frame3 = LabelFrame(window, text = "Song Playlist",padx = 5, pady = 5)
frame3.grid(row = 0, column = 1)
frame3.configure(background = "grey")

#Scrollbar For Frame 3

playsound
scroll = ttk.Scrollbar(frame3)
scroll.grid(row = 0, column = 2)



#Buttons to frame2
play_btn = Button(frame2, text = "PLAYSONG", bg = "pink",fg = "purple")
play_btn.grid(row = 1, column = 0, padx = 3)

pause_btn = Button(frame2, text = "PAUSE", bg = "pink", fg = "purple")
pause_btn.grid(row = 1, column = 1, padx = 3)

unpause_btn = Button(frame2, text = "INPAUSE", bg = "pink", fg = "purple")
unpause_btn.grid(row = 1, column = 2, padx = 3)

stop_btn = Button(frame2, text = "STOPSONG", bg = "pink",fg = "purple" )
stop_btn.grid(row = 1, column = 3, padx = 3)


window.mainloop()
