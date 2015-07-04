# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 00:06:44 2015

@author: Tommy Guan
"""
from tkinter import *
from tkinter.filedialog import askopenfilename
import smtplib

# Find Email List txt file with browser
    root = Tk()
    root.fileName = askopenfilename( filetypes = ( ("text file", "*.txt"), ("csv file", "*.csv") ) )
    root.destroy()
    
    fileName = root.fileName.replace('/', '//')
    
    with open(fileName) as f:
        emaillist = f.read().splitlines()
    
# Send email to people in the list
    SERVER = "smtp.gmail.com"
    FROM = "iamtommy15@gmail.com"
    TO = emaillist # must be a list
    
    SUBJECT = "Hello!"
    TEXT = "This is a test of emailing through smtp in google."
    
    # Prepare actual message
    message = """From: %s\r\nTo: %s\r\nSubject: %s\r\n\
    
    %s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    # Send the mail
    server = smtplib.SMTP(SERVER, 587)
    server.ehlo()
    server.starttls()
    server.login(FROM, 'qhmpicyatieieaxw')
    server.sendmail(FROM, TO, message)
    server.quit()