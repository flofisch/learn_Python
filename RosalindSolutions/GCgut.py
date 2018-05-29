#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:01:20 2018

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
f.close()
##################### bis hier FASTA #########################################
# Ausgabe durch Bibliothek!!!!

Bibliothek.keys()
Bibliothek.values()

for item in Bibliothek:
    #print(item)
    #print(Bibliothek[item])
    
    

    a = Bibliothek[item]

    # Variablen zum Zählen
    i = 0
    acount = 0
    ccount = 0
    gcount = 0
    tcount = 0
    gccont = 0
    while i < len(a):
        if  a[i] == "G":
        
            gcount += 1
            i += 1
            
        elif a[i] == "C":
                
            ccount += 1
            i += 1
        else:
            i += 1
        # Hier die berechnung des GC contents. über item wird der key aufgerufen        
        if 100*(gcount+ccount)/len(a) > gccont:
            gccont = 100*(gcount+ccount)/len(a)
            name = item

print(name)
print(100*(gcount+ccount)/len(a))
    
