import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # 열, 행

store = []
dq = []
todo = 0
for i in range(N):
    row = list(map(int, input().strip().split()))
    for j, val in enumerate(row):
        if val == 1:
            dq.append((i, j))
        elif val == 0:
            todo += 1
    store.append(row)

cnt = 0
while dq:
    cnt += 1
    tmp = []
    for x, y in dq:
        for dx, dy in [(0,1), (0,-1), (1,0), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M:
                cur = store[nx][ny] 
                if cur == -1: continue
                if cur == 0:
                    store[nx][ny] = 1
                    todo -= 1
                    tmp.append((nx, ny))
    dq = tmp

if todo > 0:
    print(-1)
else:
    print(cnt - 1)


