# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:16:29 2020

@author: Logan Rowe

Given the string, check if it is a palindrome.

Example

For inputString = "aabaa", the output should be
checkPalindrome(inputString) = true;
For inputString = "abac", the output should be
checkPalindrome(inputString) = false;
For inputString = "a", the output should be
checkPalindrome(inputString) = true.
Input/Output

[execution time limit] 4 seconds (py3)

[input] string inputString

A non-empty string consisting of lowercase characters.

Guaranteed constraints:
1 ≤ inputString.length ≤ 105.

[output] boolean

true if inputString is a palindrome, false otherwise.
"""

def checkPalindrome(inputString):
	
	if len(inputString)==1:
		return True
	for i in range(int(len(inputString)/2)+1):
		if inputString[i]!=inputString[-1-i]:
			return False
	return True