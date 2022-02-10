"""
There is a single positive integer T on the first line of input (equal to about 100000). 
It stands for the number of numbers to follow. 
Then there are T lines, each containing exactly one positive integer number N, 1≤N≤109.

For every number N, output a single line containing the single non-negative integer Z(N).
"""

t=int(input())
for i in range(t):
    x=int(input())
    y=0
    while(x>=5):
        x=x//5
        y+=x
    print(y)