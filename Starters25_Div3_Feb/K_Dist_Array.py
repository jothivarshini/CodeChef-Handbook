"""
An array is said to be good if all its elements are distinct, i.e. no two elements of the array are equal to each other.

You are given a positive integer N and an integer K such that N≤K≤(N+12).

Construct an array A of length N that satisfies the following conditions

A has exactly K good (contiguous) subarrays, and
Every element of A is an integer from 1 to N (both inclusive).
If there are multiple such arrays, you can print any of them.

Note: It can be shown that for all inputs satisfying the given constraints, there is always a valid solution
"""

for _ in range(int(input)):
    n,m=map(int,input().split())
    arr=[]
    arr.append(1)
    m-=n
    current=2
    for i in range(2,n+1):
        if m<len(arr):
            value=arr[len(arr)-k-1]
            arr.append(value)
            break
        m -=len(arr)
        arr.append(current)
        current+=1
    while(len(arr)<n):
        arr.append((arr[-1]))
    print(*arr,sep=' ')