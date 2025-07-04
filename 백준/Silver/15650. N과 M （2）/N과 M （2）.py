import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())


def recur(start, path, visited):
    if len(path) == M:
        print(' '.join(map(str,path)))
        return
    
    for i in range(start, N + 1):
        if not visited[i]:
            visited[i] = 1
            recur(i + 1, path + [i], visited)
            visited[i] = 0

recur(1, [], [0] * (N + 1))

