# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 08:57:15 2021
@author: howez
Average and Worst Case Time Complexity Analysis for Original Quick Sort
"""

from Patition_Original_July17_Counter import main
import numpy as np

#Average case
P1 = np.random.randint(1,1000000,100)

P2 = np.random.randint(1,1000000,500)

P3 = np.random.randint(1,1000000,1000)

P4 = np.random.randint(1,1000000,3000)

#sorted cases
P1_w = sorted(np.random.randint(1,1000000,100))

P2_w = np.random.randint(1,1000000,500)

P3_w = np.random.randint(1,1000000,1000)

P4_w = np.random.randint(1,1000000,3000)

#see if reversely sorted array generate same time complexity
P1_w2 = sorted(np.random.randint(1,1000000,100), reverse=True)

P2_w2 = sorted(np.random.randint(1,1000000,500), reverse=True)

P3_w2 = sorted(np.random.randint(1,1000000,1000), reverse=True)

P4_w2 = sorted(np.random.randint(1,1000000,3000), reverse=True)

print("Average, worst sorted, worst reversely sorted:")
print("100 integers")
main(P1)
main(P1_w)
main(P1_w2)

print("500 integers")
main(P2)
main(P2_w)
main(P2_w2)

print("1000 integers")
main(P3)
main(P3_w)
main(P3_w2)

print("3000 integers")
main(P4)
main(P4_w)
main(P4_w2)
