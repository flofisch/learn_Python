#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 14 13:50:38 2018

@author: S1673018
"""

#input1 = open("file6in.txt", "r")
out1 = open("file6out.txt", "w")

with open("file6in.txt") as input1:
    input2 = input1.read().splitlines()

#letters = input1.readline() 
#length = input1.readline()
#letters given
letters = input2[0].split()
#Number/length of charakters in a word
length = int(input2[1]) 
   
#number of letters:
nmbroflet = len(letters)

#Number of possible Combinations
nmbrcomb = nmbroflet**length
#print(letters[0],letters[1])

i = 0
j = 0
k = 0
while k <= nmbrcomb+2:
    k += 1
    if i < nmbroflet:
        print(letters[j],letters[i])
        out1.write(letters[j])
        out1.write(letters[i])
        out1.write("\n")
        i += 1
    else: 
        j += 1
        i = 0

out1.close()
