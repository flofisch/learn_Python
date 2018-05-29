#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 14:34:14 2018

@author: S1673018
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 11:05:10 2018

@author: S1673018
"""

#header soll Rosalind und Nummer beinhalten ohne <


#bp soll Basenpaare enthalten ohne Zeilenumbruch
# seq sind die einzelnen Zeilen der bps

f = open('text', 'r')
lines = f.readlines()
#print(lines)
bp = 0
i = 0
len(lines)

#da weise ich den namen ihre sequenzen zu
Bibliothek ={}


#Liest den ganzen bums ein

while i < len(lines): 
    #print(lines[i])
    seq = lines[i]


    #erkennt ob Zeilenanfang >
    if seq[0] == '>':
        header = seq[1:-1]
        a = "not"
    elif seq[0] != '>':
        if a == "not":
            a = seq[:-1]
        else:
            a += (seq[:-1])
        
        Bibliothek[header] = a
    i += 1
############################################################

for item in Bibliothek:
    a = Bibliothek[item]
    
    for item in Bibliothek:
        b = Bibliothek[item]
        if b[:3] == a[:3] or b[-3:] == a[:-3:] or b[:3] == a[-3:] or b[-3:] == a[:3]:
            Bibliothek.keys()
            print("Hurra eins gefunden!")
        
Bibliothek.keys()
Bibliothek.items()
Bibliothek.values()

