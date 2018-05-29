#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 14:57:06 2018

@author: S1673018
"""

# Einlesen der Daten:
#a = "AGCTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTGGATTAAAAAAAGAGTGTCTGATAGCAGC"

#print(a[0] == "A")

#print(a[1])


# list() macht eine Liste daraus

#print(list(a))


#Länge von a
#print(len(a))



#Einlesen der Datei
b = open("file1.csv")
a = b.read()
print(a)

# Variablen zum Zählen
i = 0
acount = 0
ccount = 0
gcount = 0
tcount = 0

while i < len(a):
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
        i += 1
    else:
        print("Error")


print(acount, ccount, gcount, tcount)

#easiest way to solve    
print(a.count("A"), a.count("C"), a.count("G"), a.count("T"))
