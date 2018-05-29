#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  9 16:47:13 2018

@author: S1673018
"""

b = open("file3.csv")
s = b.read()
#s = "AAAACCCGGT"

#print(s.replace("T", "a"), s.replace("A", "t"), s.replace("C", "g"), s.replace("G", "c"))

V1 = s.replace("T", "a")
V2 = V1.replace("A", "t")
V3 = V2.replace("C", "g")
V4 = V3.replace("G", "c")
V5 = V4.upper()
print(V5[::-1])

#Better in one Line
#s=s.replace("A", "t").replace .... .upper()[::-1]