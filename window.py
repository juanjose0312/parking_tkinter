# Here is the parent class structure for the other windows of tkinter
from tkinter import *

class Window:

    def __init__(self, window, title, geometry):
        self.wind = window
        self.wind.title(title)
        self.wind.geometry(geometry)

        # button that destroys the window

        Button(self.wind, text= 'volver', command= window.destroy).grid(row=9, column=1)