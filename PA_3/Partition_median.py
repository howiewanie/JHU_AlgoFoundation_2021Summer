# -*- coding: utf-8 -*-
"""
Median of Array as Pivot Quicksort
Created on Sat Jul 17 17:28:03 2021
@author: howez
"""
#using median position in an array for quick sort

def QUICKSORT(A,p,r):
    if len(A) == 1:
        return A
    if p<r:
        q = PARTITION(A,p,r)
        QUICKSORT(A,p,q-1)
        QUICKSORT(A,q+1,r)

def PARTITION(A,p,r):

        k = (p + r)//2
        #find the median
        if A[k] < A[p] and A[k] < A[r]:
            Median = min(A[p],A[r])
        elif A[k] > A[p] and A[k] > A[r]:
            Median = max(A[p],A[r])
        else:
            Median = A[k]
        #moving the median element with the next to last element and make it pivot
        A[A.index(Median)],A[r] =  A[r],A[A.index(Median)]
        
        #follow with standard partition
        i=p-1
        for j in range(p,r):
            if A[j]<=Median:
                i=i+1
                A[i],A[j] =  A[j],A[i] 
    
        A[i+1],A[r] = A[r],A[i+1]
        return (i+1)


arr = [4,3,2,1,9,10,5]
n = len(arr)
QUICKSORT(arr, 0, n-1)
print(arr)