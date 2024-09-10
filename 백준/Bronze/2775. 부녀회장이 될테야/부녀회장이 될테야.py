import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):  
    k = int(input()) 
    n = int(input())  
    
    fst = [x for x in range(1, n+1)]  
    for el in range(k):  
        for i in range(1, n):  
            fst[i] += fst[i-1]  
    print(fst[-1])  