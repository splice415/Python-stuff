# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 22:40:32 2015

@author: Tommy Guan
"""


# method 1
import pandas as p
lines = p.read_csv("B:/Users/Tommy Guan/Desktop/email.txt",header=None)
print(lines)

# method 2
with open("B:/Users/Tommy Guan/Desktop/email.txt") as f:
    email = f.read().splitlines()
    
print(email)



