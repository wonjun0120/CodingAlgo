import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
nums = sorted(list(map(int, input().strip().split())))

def recur (path, visited):
    if len(path) == M:
        print(' '.join(map(str, path)))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recur(path + [nums[i]], visited)
            visited[i] = False

recur([], [False] * N)