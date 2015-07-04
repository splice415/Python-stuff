# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 20:56:30 2015

@author: Tommy Guan
"""

"""
.open("filename", "mode")
"""
    my_list = [i**2 for i in range(1,11)]
    # Generates a list of squares of the numbers 1 - 10
    
    f = open("output.txt", "w") # open output.txt in "w" mode (write). Store in f
    
    for item in my_list:
        f.write(str(item) + "\n")
    
    f.close() # Needs to close everytime

"""
.write("str")
"""
    # "r+" = read and write
    my_list = [i**2 for i in range(1,11)]
    
    my_file = open("output.txt", "r+")
    
    # Add your code below!
    for i in my_list:
        my_file.write(str(i) + "\n")
    my_file.close()

"""
.read()
"""
    my_file = open("output.txt", "r")
    
    print(my_file.read())
    my_file.close()

"""
.readline():Read between lines
"""
    my_file = open("text.txt", "r")
    print(my_file.readline()) # 1st line
    print(my_file.readline()) # 2nd line
    print(my_file.readline()) # 3rd line
    my_file.close()
    
"""
must close write() file to write
"""
    # Open the file for reading
    read_file = open("text.txt", "r")
    
    # Use a second file handler to open the file for writing
    write_file = open("text.txt", "w")
    # Write to the file
    write_file.write("Not closing files is VERY BAD.")
    
    write_file.close()
    
    # Try to read from the file
    print(read_file.read())
    read_file.close()
    
"""
Auto-close files:'with' and 'as' keywords
"""
    with open("text.txt", "w") as textfile:
    	textfile.write("Success!")

"""
Check if file is actually closed
"""
    with open("text.txt", "w") as my_file:
        my_file.write("Sup!")
        
    if my_file.closed == False:
        my_file.close()
        
    print my_file.closed