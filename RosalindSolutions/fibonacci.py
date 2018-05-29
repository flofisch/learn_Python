#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 22 14:51:08 2018

@author: S1673018
"""

def fib(n):
    if n<2:
        return n
    else:    
        return fib(n-1)+fib(n-2)

var = fib(20)
