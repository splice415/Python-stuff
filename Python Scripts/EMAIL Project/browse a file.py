# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 23:10:47 2015

@author: Tommy Guan
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
root = Tk()
root.fileName = askopenfilename( filetypes = ( ("text file", "*.txt"), ("csv file", "*.csv") ) )
root.destroy()

fileName = root.fileName.replace('/', '//')

with open(fileName) as f:
    emaillist = f.read().splitlines()
    
print(emaillist)
