from os import *

location = ('C:\\Users\\sangh\\Desktop\\Python\\MP3 Player')
for dirpath, dirnames, filenames in walk(location):  
    print(filenames)
