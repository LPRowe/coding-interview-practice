# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 16:15:58 2020

@author: Logan Rowe

Given a year, return the century it is in. The first century spans from the year 1 up to and including the year 100, the second - from the year 101 up to and including the year 200, etc.

Example

For year = 1905, the output should be
centuryFromYear(year) = 20;
For year = 1700, the output should be
centuryFromYear(year) = 17.
"""

def centuryFromYear(year):
	year=str(year)
	L=len(year)
	if L==4:
		if year[-2:]=='00':
			cent=int(year[:2])
		else:
			cent=int(year[:2])+1
	elif L==3:
		if year[-2:]=='00':
			cent=int(year[:1])
		else:
			cent=int(year[:1])+1
	else:
		cent=1
	return cent


