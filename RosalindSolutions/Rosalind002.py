#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:04:02 2018

@author: S1673018
"""

#a = list("GATGGAACTTGACTACGTAAATT")
b = open("file1.csv")
c = b.read()
a = list(b.read())

# Variablen zum Zählen
i = 0
acount = 0
ccount = 0
gcount = 0
tcount = 0


while i < len(c):
    if a[i] == "A":
        
        acount += 1
        i += 1
    
    elif a[i] == "G":
        
        gcount += 1
        i += 1
    
    elif a[i] == "C":
        
        ccount += 1
        i += 1
    elif a[i] == "T":
        
        tcount += 1
        a[i] = "U"
        i += 1
    else:
        print("Error")
        
print(a)
b = ''.join(a)
print(b)
#b=(a[0:len(a)])
#print(b)
#print(list(a))
#print(a)
#print(acount, ccount, gcount, tcount)
