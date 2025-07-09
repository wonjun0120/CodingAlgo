import sys
from collections import deque

input = sys.stdin.readline

res = []
def recur(nums, N, M, path, visited):
    if len(path) == M:
        cur = ' '.join(map(str, path))
        if cur not in res:
            print(cur)
            res.append(cur)
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            recur(nums, N, M, path + [nums[i]], visited)
            visited[i] = False


N, M = map(int, input().strip().split())
nums = sorted(list(map(int, input().strip().split())))
recur(nums, N, M, [], [False] * N)


