#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 18:03:46 2018

@author: S1673018
"""


'''
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 
'''
f = open('text1', 'r')
b = f.readlines()
#a = "AATTAATT"
a = b[0]
len(a)
type(a)


prot = {"UUU" : "F",      "CUU" : "L",      "AUU" : "I",      "GUU" : "V",
        "UUC" : "F",      "CUC" : "L",      "AUC" : "I",      "GUC" : "V",
        "UUA" : "L",      "CUA" : "L",      "AUA" : "I",      "GUA" : "V",
        "UUG" : "L",      "CUG" : "L",      "AUG" : "M",      "GUG" : "V",
        "UCU" : "S",      "CCU" : "P",      "ACU" : "T",      "GCU" : "A",
        "UCC" : "S",      "CCC" : "P",      "ACC" : "T",      "GCC" : "A",
        "UCA" : "S",      "CCA" : "P",      "ACA" : "T",      "GCA" : "A",
        "UCG" : "S",      "CCG" : "P",      "ACG" : "T",      "GCG" : "A",
        "UAU" : "Y",      "CAU" : "H",      "AAU" : "N",      "GAU" : "D",
        "UAC" : "Y",      "CAC" : "H",      "AAC" : "N",      "GAC" : "D",
        "UAA" : "Stop",   "CAA" : "Q",      "AAA" : "K",      "GAA" : "E",
        "UAG" : "Stop",   "CAG" : "Q",      "AAG" : "K",      "GAG" : "E",
        "UGU" : "C",      "CGU" : "R",      "AGU" : "S",      "GGU" : "G",
        "UGC" : "C",      "CGC" : "R",      "AGC" : "S",      "GGC" : "G",
        "UGA" : "Stop",   "CGA" : "R",      "AGA" : "R",      "GGA" : "G",
        "UGG" : "W",      "CGG" : "R",      "AGG" : "R",      "GGG" : "G" }

i=0
j=i+3
s=[]
dum=[]
while j <= len(a):
    seq = a[i:j]
    i+=3
    j=i+3
    if prot[seq] == "Stop":
        exit
    else:
        s = (prot[seq])
        dum.append(s)
        
        #print(prot[seq])
Protein = ''.join(dum)
print(Protein)
