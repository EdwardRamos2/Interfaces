#!/usr/bin/env python3

import pygame
from tkinter import *
import os
import sys

#FUNCOES
def interfaces():
    os.system('ifconfig')

#INTERFACE
gui = Tk()
gui.geometry('400x300')
gui.title('ManguePyPlay')

bto = Button(gui, text='Interfaces', command=interfaces)
bto.pack()


#MAINLOOP
gui.mainloop()
