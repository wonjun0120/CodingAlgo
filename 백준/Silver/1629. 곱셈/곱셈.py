import sys
from collections import deque

input = sys.stdin.readline

def mod_pow(a, b, c):
    if b == 0: return 1
    half = mod_pow(a, b // 2, c)
    res = half * half % c
    if b % 2 == 1:
        res = (a * res) % c
    return res

A, B, C = map(int, input().strip().split())

print(mod_pow(A, B, C))
