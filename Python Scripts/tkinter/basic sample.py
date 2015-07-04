# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 16:48:10 2015

@author: Tommy Guan
"""

import tkinter as tk

class simpleapp_tk(tk.Frame): # usually make a class for our gui
    
    def __init__(self, parent): # need to initate class with self, and parent = parent class.
        tk.Frame.__init__(self, parent) 
        self.parent = parent # give parent a variable
        self.pack()
        self.initialize() # use the initialzie() method 
        
    def initialize(self): # method to create all the GUI stuff in 
        self.grid() # our grid layout manager. 
        
        self.entry = tk.Entry(self) # create Entry widget
        self.entry.grid(column=0, row=0, sticky='EW') # put it in col 0, row 0. 
            # stick='EW' ask the widget to stick to soe edges of the cell

root = tk.Tk()
app = simpleapp_tk(parent=root)

app.mainloop() # loop indefinitely for events like clicking buttons, press keys, os asking to close, etc

