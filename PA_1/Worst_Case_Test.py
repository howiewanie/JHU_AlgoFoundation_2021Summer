# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 22:10:09 2021

@author: howez
"""
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 16 13:58:53 2021

@author: howez
"""
from June_16th_Counter import main

import random

P = [(random.random()*100.0, random.random()*100.0) for _ in range(10)]

#P = [(random.random()*100.0, random.random()*100.0) for _ in range(100)]

#P = [(random.random()*100.0, random.random()*100.0) for _ in range(10000)]

#P = [(random.random()*100.0, random.random()*100.0) for _ in range(100000)]

#P = [(random.random()*100.0, random.random()*100.0) for _ in range(1000000)]

main(P,len(P)//2)