import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
A = list(map(int, input().strip().split()))

def lower_bound(tails, size, el):
    l, r = 0, size
    while l < r:
        m = (l + r) // 2
        if tails[m] < el:
            l = m + 1
        else:
            r = m
    return l

tails = [0] * N
length = 0

for el in A:
    idx = lower_bound(tails, length, el)
    tails[idx] = el
    if idx == length:
        length += 1

print(length)

