# -*- coding: utf-8 -*-
"""
Standard Quicksort with Normal Partition
Created on Sat Jul 17 00:10:11 2021
@author: howez
"""

def QUICKSORT(A,p,r):
    if len(A) == 1:
        return A
    if p<r:
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)
        
def PARTITION(A,p,r):
    x=A[r]
    i=p-1
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j] =  A[j],A[i] 
    A[i+1],A[r] = A[r],A[i+1]
    print(A)
    return (i+1)

arr = [4,3,2,1,9,10,5]
n = len(arr)
QUICKSORT(arr, 0, n-1)
print(arr)
