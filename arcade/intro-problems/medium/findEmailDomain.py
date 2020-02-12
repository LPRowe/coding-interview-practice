# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:26:09 2020

@author: Logan Rowe

An email address such as "John.Smith@example.com" is made up of a local 
part ("John.Smith"), an "@" symbol, then a domain part ("example.com").

The domain name part of an email address may only consist of letters, digits, 
hyphens and dots. The local part, however, also allows a lot of different 
special characters. Here you can look at several examples of correct and 
incorrect email addresses.

Given a valid email address, find its domain part.

Example

For address = "prettyandsimple@example.com", the output should be
findEmailDomain(address) = "example.com";
For address = "fully-qualified-domain@codesignal.com", the output should be
findEmailDomain(address) = "codesignal.com".
Input/Output

[execution time limit] 4 seconds (py3)

[input] string address

Guaranteed constraints:
10 ≤ address.length ≤ 50.

[output] string
"""

def findEmailDomain(address):
    #find the index of the @ symbol closest to the end (although there should be only one)
    idx=address.rfind('@')
    return(address[idx+1:])
    

if __name__=='__main__':
    addresses=["fully-qualified-domain@codesignal.com","prettyandsimple@example.com"]
    for address in addresses:
        print(findEmailDomain(address))