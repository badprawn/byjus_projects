#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 10 19:50:49 2024

@author: pranavnair
"""

class watch:
    x = 5
    def __init__(self, y):
        print("This is the blueprint " + str(y))
        self.y = y
        
watchduplicate = watch(10)
print(watchduplicate.x)
print(watchduplicate.y)

