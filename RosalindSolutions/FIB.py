#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 15:59:48 2018

@author: S1673018
"""

Rabbits = 2
Month = 5
Babys = 3
'''
i = 0
while i < Month:
    Rabbits = Rabbits + (int((Rabbits/2))*3)
    i += 1
print(Rabbits)
'''
i = 0
l = 5


while i < l:
    i+=1
    adults=Rabbits
    offspring=(int(adults/2))*Babys
    Rabbits=adults+offspring
    print(Rabbits)
    
Fn = 1    
F1 = 1
F2 = 1
i=0
while i<Fn:
    Fn= (Fn-F1)+(Fn-F2)
    F1= Fn-F1
    F2= Fn-F2
    print(Fn)
    i+=1    
i=0
j=10
a=0
b=1
while i<j:
    i+=1
    print(a)
    
    V1=a+b
    a=b
    b=V1    

i=0
monate =5
klein =1
gross = 0
ges = klein
while i < monate:
    i += 1
    print("Hasen gesamt:", ges)
    print("Geschlechtsteife Tiere:", gross)
    print("Süße Hasenbabies:", klein)
    print("\n")
    gross = klein
    kinder=gross*3
    klein1=kinder
    ges=klein+gross




a=1

#1.Loop
b=a
ges=b
#2.Loop
a=b*3
ges=b+a
#3.Loop
repro=3
monate = 2
kinder=(repro**monate)+




