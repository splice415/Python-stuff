# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:31:13 2015

@author: Tommy Guan
"""
import smtplib
SERVER = "smtp.gmail.com"
FROM = "iamtommy15@gmail.com"
TO = ["hamachikama15@gmail.com"] # must be a list

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