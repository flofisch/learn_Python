#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 16 15:04:25 2018

@author: S1673018
"""


#FASTA einlesen
with open("file7in.txt") as input1:
    input2 = input1.read().splitlines()

i = 0

#while input2[i]:
#    i += 1
#    print(i)
for Rosalind in input2[i]:
    print(input2[i])
    i += 1

#Einlesen der Datei
b = open("file7.csv")
a = b.read()


a = "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
print(a)

# Variablen zum Zählen
i = 0
acount = 0
ccount = 0
gcount = 0
tcount = 0

while i < len(a):
    if  a[i] == "G":
        
        gcount += 1
        i += 1
    
    elif a[i] == "C":
        
        ccount += 1
        i += 1
    else:
        i += 1

print(100*((gcount+ccount)/len(a)))
