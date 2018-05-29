#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:53:40 2018

@author: S1673018
"""

klein =1
groß=0
wachstum=2
monate =34
i=0
#loop

while i < monate:
    i += 1
    print(klein)
    print(groß)
    print("Gesamt:", klein+groß)
    print("\n")
    baldgroß=klein+groß
    klein=groß*wachstum
    groß=baldgroß