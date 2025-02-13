# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 11:12:49 2025

@author: virha
"""

t = ([x for x in range(12345) if x ** 2 % 3 == 0 and x ** 2 % 4 == 0 and x ** 2 % 8 != 0])
print(t)