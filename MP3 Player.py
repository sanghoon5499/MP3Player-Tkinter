import pygame
from tkinter import *
from time import *
from random import *
from os import *

root = Tk()
screen = Canvas( root, width = 500, height = 650, background = "white" )
pygame.init()
pygame.mixer.init()

######################

Remove = 0
location = ('C:\\Users\\sangh\\Desktop\\Python\\MP3 Player')
for dirpath, dirnames, filenames in walk(location):  
    print(filenames)
string = (filenames)
NumItems = len(string)
for i in range(NumItems):
    item = string[Remove]
    Check = item[-3:]   
    if Check not in ["mp3"]:
        string.remove(string[Remove])
        Remove = Remove 
    else:
        Remove = Remove +1
print (string)
CurrentSong = choice(string)

#########################

xDisk = 250
yDisk = 250

Disk = PhotoImage (file='C:\\Users\\sangh\\Desktop\\Python\\MP3 Player\\MusicDisk.png')
screen.create_image(xDisk, yDisk, image=Disk, anchor=CENTER)
screen.update()

########################

def PlayButtonPressed():
    pygame.mixer.music.load(CurrentSong)
    pygame.mixer.music.play()

def PauseButtonPressed():
    pygame.mixer.music.pause()

def StopButtonPressed():
    pygame.mixer.music.stop()

def UnpauseButtonPressed():
    pygame.mixer.music.unpause()

def SkipButtonPressed():
    global CurrentSong
    if CurrentSong == "1.mp3":
        CurrentSong = "2.mp3"
    elif CurrentSong == "2.mp3":
        CurrentSong = "1.mp3"

########################

PlayButton = Button(root, text="Play", command = PlayButtonPressed)
img1 = PhotoImage(file="C:\\Users\\sangh\\Desktop\\Python\\MP3 Player\\start!.gif")
PlayButton.config(image=img1)
PlayButton.pack()
PlayButton.place( x = 15, y = 500, width = 70 )

UnpauseButton = Button(root, text="", command = UnpauseButtonPressed)
img2 = PhotoImage(file="C:\\Users\\sangh\\Desktop\\Python\\MP3 Player\\unpause.gif")
UnpauseButton.config(image=img2)
UnpauseButton.pack()
UnpauseButton.place( x = 115, y = 500, width = 70 )

PauseButton = Button(root, text="Pause", command = PauseButtonPressed)
img3 = PhotoImage(file="C:\\Users\\sangh\\Desktop\\Python\\MP3 Player\\pause.gif")
PauseButton.config(image=img3)
PauseButton.pack()
PauseButton.place( x = 215, y = 500, width = 70 )

StopButton = Button(root, text="Stop", command = StopButtonPressed)
img4 = PhotoImage(file="C:\\Users\\sangh\\Desktop\\Python\\MP3 Player\\stop.gif")
StopButton.config(image=img4)
StopButton.pack()
StopButton.place( x = 315, y = 500, width = 70 )

SkipButton = Button(root, text="Skip (broken)", command = SkipButtonPressed)
##img5 = PhotoImage(file="C:/Users/sangh/Downloads/Python/MP3 Player/skip.gif") #tf is going on here
##SkipButton.config(image=img5)
SkipButton.pack()
SkipButton.place( x = 415, y = 500, width = 80 )

########################

screen.pack()
screen.focus_set()
root.mainloop()
