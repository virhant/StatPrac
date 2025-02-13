# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 16:46:22 2025

@author: virha
"""
def count_words(str):
    return {list(str)[i] : str.count(list(str)[i]) for i in range(len(str))}

str = "hello, world!"
print(count_words(str))