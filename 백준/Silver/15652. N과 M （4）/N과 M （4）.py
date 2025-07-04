import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())


def recur(start, path):
    if len(path) == M:
        print(' '.join(map(str,path)))
        return
    
    for i in range(start, N + 1):
        recur(i, path + [i])

recur(1, [])

