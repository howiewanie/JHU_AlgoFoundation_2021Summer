# -*- coding: utf-8 -*-
"""
Created on Tue Jul 20 10:23:39 2021
Average and Worst Case Time Complexity Analysis for Median Quick Sort
@author: howez
"""


from Partition_median_Counter import main
import random

#Average case
P1 = random.sample(range(1,1000000),100)

P2 = random.sample(range(1,1000000),1000)

P3 = random.sample(range(1,1000000),10000)

P4 = random.sample(range(1,1000000),50000)

#sorted cases
P1_w = random.sample(range(1,1000000),100)

P2_w = random.sample(range(1,1000000),1000)

P3_w = random.sample(range(1,1000000),10000)

P4_w = random.sample(range(1,1000000),50000)

#see if reversely sorted array generate same time complexity

P1_w2 = sorted(random.sample(range(1,1000000),100), reverse=True)

P2_w2 = sorted(random.sample(range(1,1000000),1000), reverse=True)

P3_w2 = sorted(random.sample(range(1,1000000),10000), reverse=True)

P4_w2 = sorted(random.sample(range(1,1000000),50000), reverse=True)

print("Average, worst sorted, worst reversely sorted:")
print("100 integers")
main(P1)
main(P1_w)
main(P1_w2)

print("1000 integers")
main(P2)
main(P2_w)
main(P2_w2)

print("10000 integers")
main(P3)
main(P3_w)
main(P3_w2)

print("100000 integers")
main(P4)
main(P4_w)
main(P4_w2)
