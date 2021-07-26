# -*- coding: utf-8 -*-
"""
Standard Quicksort with Counter
Created on Sat Jul 17 00:10:11 2021
@author: howez
"""

def QUICKSORT(A,p,r,count):
    if len(A) == 1:
        return A
    if p<r:
        #print("quicksort beg-",count)
        q, count = PARTITION(A,p,r,count)
        count=QUICKSORT(A,p,q-1,count)
        count=QUICKSORT(A,q+1,r,count)
    return(count)
    

        
def PARTITION(A,p,r,count):
    x=A[r]
    i=p-1
    #print("partition beg",count)
    for j in range(p,r):
        if A[j]<=x:
            i=i+1
            A[i],A[j] =  A[j],A[i]
            count+=1
    A[i+1],A[r] = A[r],A[i+1]
    count+=1
    #print(A)
    #print("partition end",count)
    return (i+1, count)

def main(A):
    count = 0
    n = len(A)
    print(QUICKSORT(A, 0, n-1,count))
    
    
#arr = [4,3,2,1,9,10,5]
#n = len(arr)
#main(arr)
#print(arr)
