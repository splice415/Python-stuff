# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 17:44:17 2015

@author: Tommy Guan
"""

import tkinter as tk
from tkinter import ttk

LARGE_FONT = ("Verdana", 12)


class SeaofBTCapp(tk.Tk): # parent class = tkinter.Tk
    
    def __init__(self, *args, **kwargs): #args = arguments, variables. kwargs = keyword args, dictionaries.
        
        tk.Tk.__init__(self, *args, **kwargs)
        
        tk.Tk.iconbitmap(self, default="icon2.ico)    # put a dir path to the .ico file.    
        tk.Tk.wm_title(self, "Sea of BTC Client")   # give it a title        
        
        container = tk.Frame(self) # create the frame, set to container
        container.pack(side="top", fill="both", expand = True) # minimal organization, let it pack stuff in for you. 
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        
        for F in (StartPage, PageOne, PageTwo): 
            # store the pages into the frames dictionary so it would work.
            frame = F(container, self)
            
            self.frames[F] = frame
            
            frame.grid(row=0, column=0, sticky = "nsew") # alignment + stretch to north,south,east, west.
            
        self.show_frame(StartPage)
        
    
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise() # raise it to the front

     
class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page 1", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button1 = ttk.Button(self, text="Visit Page 1",  
                            command=lambda: controller.show_frame(PageOne))
                # ttk has more rounded buttons.
                            
        button1.pack() # create button 1 to page 1
        
        button2 = ttk.Button(self, text="Visit Page 2", 
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack() # create button 2  to page 2       
        
class PageOne(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Start Page", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Back to home", 
                            command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        button2 = ttk.Button(self, text="To Page 2", 
                            command=lambda: controller.show_frame(PageTwo))
        button2.pack()      
        
class PageTwo(tk.Frame):
    
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self, text="Page Two", font=LARGE_FONT)
        label.pack(pady=10, padx=10)
        
        button = ttk.Button(self, text="Back to home", 
                            command=lambda: controller.show_frame(StartPage))
        button.pack()
        
        button1 = ttk.Button(self, text="Back to Page 1", 
                            command=lambda: controller.show_frame(PageOne))
        button1.pack()
    
app = SeaofBTCapp()
app.mainloop()