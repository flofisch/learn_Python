#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 11 10:53:46 2018

@author: S1673018
"""

# dominant:
d = 16
# hetero:
h = 22
# recessive:
r = 20

# dominant tree:
ast1 = (d/(d+h+r))
Baum1 = ast1
ast2 = (h/(d+h+r))
ast3 = (r/(d+h+r))

# hetero tree:
Baum2 = (ast2*0.5)*(1+(d/(d+h+r-1))+((h-1)/(d+h+r-1))*0.5)


# recessive tree:
Baum3 = ast3*((d/(d+h+r-1))+((h/(d+h+r-1))*0.5))

print(Baum1+Baum2+Baum3)
