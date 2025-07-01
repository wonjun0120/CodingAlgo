import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
statements = list(map(int, input().strip().split()))

dq = deque(range(1, N + 1))

cnt = 0
for el in statements:
    idx = dq.index(el)

    if idx <= len(dq) // 2:
        dq.rotate(-idx)
        cnt += idx

    else:
        dq.rotate(len(dq) - idx)
        cnt += (len(dq) - idx)
    
    dq.popleft()

print(cnt)