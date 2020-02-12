# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 15:17:23 2020

@author: Logan Rowe

Check if the given string is a correct time representation of the 24-hour clock.

Example

For time = "13:58", the output should be
validTime(time) = true;
For time = "25:51", the output should be
validTime(time) = false;
For time = "02:76", the output should be
validTime(time) = false.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string time

A string representing time in HH:MM format. It is guaranteed that the first 
two characters, as well as the last two characters, are digits.

[output] boolean

true if the given representation is correct, false otherwise.
"""

def validTime(time):
    hour,minute=time.split(':')
    hour,minute=int(hour),int(minute)
    
    if 0<=hour and hour<=23 and 0<=minute and minute<=59:
        return True
    return False
    
    
    
    
    
    
if __name__=='__main__':
    times=['13:58','25:51']
    for time in times:
        print(validTime(time))