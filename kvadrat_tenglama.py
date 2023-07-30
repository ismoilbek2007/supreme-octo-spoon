# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 09:41:57 2023

@author: hp
"""
import math
a = int(input('a ni kiriting:'))
b = int(input('b ni kiriting:'))
c = int(input('c ni kiriting:'))
d = math.sqrt(b**2-4*a*c)
if d>0:
    x1 = (-b+d)/(2*a)
    x2 = (-b-d)/(2*a)
    print(x1,x2)
elif d==0:
    x1 = (-b+d)/(2*a)
    print(x1)
else:
   print("Tenglama yechimga ega emas!")
    
    
        
