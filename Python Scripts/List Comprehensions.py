# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 01:39:35 2015

@author: Tommy Guan
"""

"""Print even numbers
"""
    evens_to_50 = [i for i in range(51) if i % 2 == 0]
    print(evens_to_50)
    
"""Doubled numbers evenly divible by two, three, four
"""
    doubles_by_3 = [x*2 for x in range(1,6) if (x*2) % 3 == 0] # divible by 3
    
    # Complete the following line. Use the line above for help.
    even_squares = [x**2 for x in range(1,12) if x%2 == 0] # divisible by 2
    print(even_squares)
    
    # Cubes of numbers 1 through 10 only if cube is evenly divisible by four.
    cubes_by_four = [x**3 for x in range(1,11) if (x**3)%4 == 0]
    print(cubes_by_four)

    # Comprehension list into a filter with lambda function
    squares = [x**2 for x in range(1,11)]
    print(filter(lambda x: 30 <= x <= 70, squares ))
    
    
"""Slicing
"""
    # Print out only odd numbers from 1-10
    my_list = range(1, 11) # List of numbers 1 - 10
    
    # Add your code below!
    print my_list[::2]
    
    #Reversing a list
    my_list = range(1, 11)
    backwards = my_list[1::-1]
    
    # Reverse list by 10
    to_one_hundred = range(101)
    backwards_by_tens = to_one_hundred[::-10]
    print backwards_by_tens

    # odds and middle slices
    to_21 = range(1,22) # 1 to 21
    odds = to_21[::2] # 1,3,5,...,21
    middle_third = to_21[(len(to_21)/3):((len(to_21)/3)*2)] # 8,9,...,14
    
    # if with or
    threes_and_fives = [i for i in range(1,16) if i%3==0 or i%5==0]    
    
"""Lambdas. similar to function(x) of apply() in R.
"""
    my_list = range(16)
    print(filter(lambda x: x % 3 == 0, my_list)) # only takes mod 3 from 0-15.
    
    #Backward and Remove X's
    garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

    message = filter(lambda x: x != "X", garbled)
    print(message)

    languages = ["HTML", "JavaScript", "Python", "Ruby"]
    print filter(lambda x: x == "Python", languages) #returns only Python