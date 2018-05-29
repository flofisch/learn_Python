#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:45:21 2018

@author: S1673018
"""

b = open("file5.csv")
STR1 = b.readline()
#check document for empty lines before you read it!
STR2 = b.readline()

#andere Aufgabe
#V1 = STR2.replace("T", "a")
#V2 = V1.replace("A", "t")
#V3 = V2.replace("C", "g")
#V4 = V3.replace("G", "c")
#V5 = V4.upper()

i = 0
j = 0
while i < len(STR1)-1:
    if STR1[i]!=STR2[i]:
        j += 1
        i += 1
        #print(i)
    else:
        i += 1
print(j)
#shorter solution
print([a!=b for (a, b) in zip(STR1, STR2)].count(True))
#even shorter
sum([a != b for a, b in zip(STR1, STR2)])
        