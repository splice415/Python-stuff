# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 01:13:49 2015

@author: Tommy Guan
"""

"""Item, Keys, Values for Dictionaries
"""
    my_dict = {
        "Name": "Guido",
        "Age": 56,
        "BDFL": True,
        "Gamer": True
    }
    
    print(my_dict.items())
    
    print(my_dict.keys()) 
    print(my_dict.values())

"""Print letters on same lines
"""
    for letter in "Eric":
        print(letter, end=" ")

    for key in my_dict:
        print(key, my_dict[key])
        

