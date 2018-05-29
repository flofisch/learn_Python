#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 10:43:43 2018

@author: S1673018
"""
f = open("text2","r")
b = f.readline()
b[2]
a = b.split()
V1 = 0
V2 = 0
V3 = 0
V4 = 0
V5 = 0
V6 = 0
    
V1 = int(a[0])*2
V2 = int(a[1])*2
V3 = int(a[2])*2
V4 = int(a[3])*1.5
V5 = int(a[4])
V6 = 0

print(V1 + V2 + V3 + V4 + V5 + V6)


