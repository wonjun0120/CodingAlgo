import sys
from collections import deque

input = sys.stdin.readline

res = []
def recur(start, nums, N, M, path, visited):
    if len(path) == M:
        cur = ' '.join(map(str, path))
        if cur not in res:
            print(cur)
            res.append(cur)
        return
    
    for i in range(start, N):
        recur(i, nums, N, M, path + [nums[i]], visited)


N, M = map(int, input().strip().split())
nums = sorted(list(map(int, input().strip().split())))
recur(0, nums, N, M, [], [False] * N)


