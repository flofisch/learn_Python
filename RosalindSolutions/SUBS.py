#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 15:03:51 2018

@author: S1673018
"""

#STR1 = "GATATATGCATATACTT"
#STR2 = "ATAT"

b = open("file4.csv")
STR1 = b.readline()
#check document for empty lines before you read it!
STR2 = b.readline()


#STR1[2:5]

#STR1.find(STR2)
 #   STR1[i]==STR2
    
i=0
j=i+len(STR2)    
anzahl = 0
while j < len(STR1):
    if STR1[i:j]==STR2:
        print(i+1)
        #anzahl += 1
        i += 1
        j += 1
    else:
        i += 1
        j += 1
print(anzahl)

#shorter solution
r = 0
while r != -1 :
    r = STR1.find(STR2,r+1)
    print(r+1)

    