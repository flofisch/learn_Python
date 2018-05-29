#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 24 11:17:38 2018

@author: S1673018
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 23 17:53:40 2018

@author: S1673018
"""

klein =1
groß=0
wachstum=2
monate =6
i=0
j=0
tod1=0
tod2=0
tod3=0
tod4=0
tod5=0
tod6=0
tod7=0
tod8=0
tod9=0
tod10=0
tod11=0
tod12=0
tod13=0
tod14=0
tod15=0
tod16=0
tod17=0
tod18=0
tod19=0
tod20=0
#loop

while i < monate:
    i += 1
    
    
    tod20=tod19
    tod19=tod18
    tod18=tod17
    tod17=tod16
    tod16=tod15
    tod15=tod14
    tod14=tod13
    tod13=tod12
    tod12=tod11
    tod11=tod10
    tod10=tod9
    tod9=tod8
    tod8=tod7
    tod7=tod6
    tod6=tod5
    tod5=tod4
    tod4=tod3
    tod3=tod2
    tod2=tod1
    tod1=klein
    
    print(klein)
    print(groß)
    print("Gesamt:", klein+groß)
    print("\n")
    baldgroß=klein+groß
    klein=(groß-tod4)*wachstum
    groß=baldgroß-tod4