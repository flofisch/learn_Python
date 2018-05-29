#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 16:03:49 2018

@author: S1673018
"""
'''
a = 3
b = a-(a-1)
b= ()
i=1
#Liste anlegen

#Fakultät berechnen
summe = 1
i = 1
while(i < a+1):
    summe = summe *i
    i += 1
print(summe)

#Liste of möglichen Positionen
#Versuch
#Rows also Spalten, die 
R1 = 0
R2 = 1
R3 = 2
Zahl = 0
while Zahl <= summe-1:
    #print(lst[R1], lst[R2], lst[R3])
    Zahl += 1
    if R1 < 2 and R1 != R2 and R1 != R3 and R2 != R3:
        print(lst[R1], lst[R2], lst[R3])
        print(lst[R3], lst[R2], lst[R1])
        R1 += 1
        R2 += 1
        R3 -= 2
    else:
        R2 -= 3
        R3 += 3
#        print(R1, R2, R3)
        print(lst[R1], lst[R2], lst[R3])
        print(lst[R3], lst[R2], lst[R1])
'''        



#Datei öffnen   
f = open("file5.txt", "w")   

#Liste anlegen     
a = 7
lst=[]
i=1
while i <= a:
    lst.append(i)
    i += 1
print(lst)
    


#Fakultät berechnen
summe = 1
i = 1
while(i < a+1):
    summe = summe *i
    i += 1
print(summe)
f.write(str(summe))

#permutationen anzeigen
#hier muss ich noch die leerzeichen, bzw. die zeilenumbrüche einfügen
import itertools
lst2 = list(itertools.permutations(lst))
f.write('\n')
j = 0
var1 = []
var2 = []
while j <= summe-1:
    #print(lst2[j])
    
#    f.write(str(lst2[j]))
    var1 = lst2[j]
#    f.write(var1.join())
#    print(str(lst2[j]))
    print(var1[0], var1[1], var1[2])
    f.write('{}'.format(var1[0]))
    f.write(' ')
    f.write('{}'.format(var1[1]))
    f.write(' ')
    f.write('{}'.format(var1[2]))
    
    f.write(' ')
    f.write('{}'.format(var1[3]))
    f.write(' ')
    f.write('{}'.format(var1[4]))
    f.write(' ')
    f.write('{}'.format(var1[5]))
    f.write(' ')
    f.write('{}'.format(var1[6]))
    
#    var2 = str(var1)
#    "".join(var2[0])
    
    f.write('\n')
    j +=1  
f.close()    
