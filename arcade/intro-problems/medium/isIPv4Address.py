# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 01:19:10 2020

@author: Logan Rowe

An IP address is a numerical label assigned to each device 
(e.g., computer, printer) participating in a computer network that uses the 
Internet Protocol for communication. There are two versions of the Internet 
protocol, and thus two versions of addresses. One of them is the IPv4 address.

Given a string, find out if it satisfies the IPv4 address naming rules.

Example

For inputString = "172.16.254.1", the output should be
isIPv4Address(inputString) = true;

For inputString = "172.316.254.1", the output should be
isIPv4Address(inputString) = false.

316 is not in range [0, 255].

For inputString = ".254.255.0", the output should be
isIPv4Address(inputString) = false.

There is no first number.

Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A string consisting of digits, full stops and lowercase English letters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 30.

[output] boolean

true if inputString satisfies the IPv4 address naming rules, false otherwise.



Notes:
    IPv4 address is a string with the following structure: a.b.c.d, where 
    a, b, c and d are integers in range [0, 255]. For example, 0.0.0.0, 
    255.255.255.255 or 252.0.128.32 are correct IPv4 addresses, and 0.0.0.256, 
    -1.1.1.1, 0.0.0.0.0 are incorrect.

    a.b is named network part and c.d is named host part.
"""

'''
Thoughts:
    
1) split IP by '.'
2) convert each item to integer and check if it is between 0 and 255 inclusive
3) ensure list is only 4 items long

'''

def isIPv4Address(inputString):
    components=inputString.split('.')
    
    for i in components:
        try:
            int(i)
        except:
            return False
        if int(i)>255 or int(i)<0:
            return False
        if len(components)!=4:
            return False
                
    return True


if __name__=='__main__':
    IPs=["172.16.254.1","172.316.254.1",".254.255.0"]
    output=[True,False,False]
    
    for (i,j) in zip(IPs,output):
        if isIPv4Address(i)==j:
            print("passed test")
        else:
            print('failed:',i)