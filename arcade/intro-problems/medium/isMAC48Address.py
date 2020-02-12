# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 14:12:26 2020

@author: Logan Rowe

A media access control address (MAC address) is a unique identifier assigned 
to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly 
form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by 
hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to 
MAC-48 address or not.

Example

For inputString = "00-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = true;
For inputString = "Z1-1B-63-84-45-E6", the output should be
isMAC48Address(inputString) = false;
For inputString = "not a MAC-48 address", the output should be
isMAC48Address(inputString) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

Guaranteed constraints:
15 ≤ inputString.length ≤ 20.

[output] boolean

true if inputString corresponds to MAC-48 address naming rules, false otherwise.
"""

import string

def isMAC48Address(inputString):
    #First let us check that the input is in 6 groups of 2 characters separated by '-'
    sub_strings=inputString.split('-')
    if len(sub_strings)!=6:
        return False
    for s in sub_strings:
        if len(s)!=2:
            return False
    
    #Now lets check whether the substring consists of all valid characters
    valid_characters=string.hexdigits
    
    for character in inputString:
        if character not in valid_characters and character!='-':
            return False
    
    return True
    
    
    
if __name__=="__main__":
    inputs=["00-1B-63-84-45-E6","Z1-1B-63-84-45-E6"]
    for s in inputs:
        print(isMAC48Address(s))