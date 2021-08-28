# -*- coding: utf-8 -*-
"""
Median of Array as Pivot Quicksort with Counter
Created on Sat Jul 17 17:28:03 2021
@author: howez
"""
#using median position in an array for quick sort

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

        k = (p + r)//2
        count+=1
        #find the median
        if A[k] < A[p] and A[k] < A[r]:
            Median = min(A[p],A[r])
            count+=1
        elif A[k] > A[p] and A[k] > A[r]:
            Median = max(A[p],A[r])
            count+=1
        else:
            Median = A[k]
            count+=1
        #moving the median element with the next to last element and make it pivot
        A[A.index(Median)],A[r] =  A[r],A[A.index(Median)]
        count+=1
        
        #follow with standard partition
        i=p-1
        for j in range(p,r):
            if A[j]<=Median:
                i=i+1
                count+=1
                A[i],A[j] =  A[j],A[i]
    
        A[i+1],A[r] = A[r],A[i+1]
        count+=1
        return (i+1, count)
    
def main(A):
    count = 0
    n = len(A)
    print(QUICKSORT(A, 0, n-1,count))
    
    
arr = [4,3,2,1,9,10,5]

n = len(arr)
main(arr)
print(arr)
