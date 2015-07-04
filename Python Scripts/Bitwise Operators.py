# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 16:27:04 2015

@author: Tommy Guan
"""

"""Basic about Binary/Bits
"""
    print 5 >> 4  # Right Shift 0
    print 5 << 1  # Left Shift  10
    print 8 & 5   # Bitwise AND 0
    print 9 | 4   # Bitwise OR  13
    print 12 ^ 42 # Bitwise XOR 38
    print ~88     # Bitwise NOT -89
    
    8's bit  4's bit  2's bit  1's bit
        1       0       1      0 
        8   +   0    +  2   +  0  = 10 
        
    2**0 = 1 
    2**1 = 2
    2**2 = 4
    2**3 = 8
    2**4 = 16
    2**5 = 32
    2**6 = 64
    2**7 = 128
    2**8 = 256
    2**9 = 512
    2**10 = 1024
    
    one = 0b1
    two = 0b10
    three = 0b11
    four = 0b100
    five = 0b101
    six = 0b110
    seven = 0b111
    eight = 0b1000
    nine = 0b1001
    ten = 0b1010
    eleven = 0b1011
    twelve = 0b1100

# Can use bin(x) function to see binary representation of x as a string.

"""Use int(str, base=10) to get base 10 representations.
"""
    print(int("1",2))           # 1
    print(int("10",2))          # 2
    print(int("111",2))         # 7
    print(int("0b100",2))       # 4
    print(int(bin(5),2))        # 5
    print(int("11001001", 2))   # 201

"""Shifts
"""
# Left Bit Shift (<<)  
    0b000001 << 2 == 0b000100   # (1 << 2 = 4)
    0b000101 << 3 == 0b101000   # (5 << 3 = 40)       
    
    # Right Bit Shift (>>)
    0b0010100 >> 3 == 0b000010  # (20 >> 3 = 2)
    0b0000010 >> 2 == 0b000000  # (2 >> 2 = 0)
    
    shift_right = 0b1100
    shift_left = 0b1
    
    shift_right = shift_right >> 2  # 0b11
    shift_left = shift_left << 2    # 0b100
    
""" AND (&) Bit Operator
"""
         a:   00101010   42
         b:   00001111   15       
    ===================
     a & b:   00001010   10
     
    0b111 (7) & 0b1010 (10) = 0b10 (2)
    
    print(bin(0b1110 & 0b101))  # "0b100"

""" OR (^) Bit Operator
"""
        a:  00101010  42
        b:  00001111  15       
    ================
    a | b:  00101111  47
    
     110 (6) | 1010 (10) = 1110 (14)
     
     print(bin(0b1110 | 0b101))     # "0b1111"
     
""" XOR (^) or Exclusive OR Bit Operator
"""
        a:  00101010   42
        b:  00001111   15       
    ================
    a ^ b:  00100101   37
    
    111 (7) ^ 1010 (10) = 1101 (13)
    
    print(bin(0b1110 ^ 0b101))  # "0b1011"
    
""" NOT (~) Bit Operator
"""
    # Add 1 to number then turn it negative
    print(~1)   # -2
    print(~2)   # -3
    print(~3)   # -4
    print(~42)  # -43
    print(~123) # -124
    
"""Bit Mask, check a certain bit is on
"""
    def check_bit4(input):
        mask = 0b1000   # Check if fourth bit is on
        y = input & mask
        if y > 0:
            return "on"
        else:
            return "off"

    # Turn on a bit with Mask
    a = 0b10111011
    mask = 0b100
    desired = a | mask
    print(bin(desired)) # "0b10111111"
    
    #Flip bits
    a = 0b11101110
    mask = 0b11111111
    desired = a ^ mask
    print(bin(desired)) # "0b10001"
    
    # Flip bits with shift
    def flip_bit(number, n):
        mask = 0b1 << (n-1)
        result = number ^ mask
        return bin(result)

