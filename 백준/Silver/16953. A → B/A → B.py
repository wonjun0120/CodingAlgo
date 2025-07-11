import sys
from collections import deque

input = sys.stdin.readline

A, B = map(int, input().strip().split())

dq = deque([(A, 1)])

while dq:
    cur, num = dq.popleft()

    if cur == B:
        print(num)
        sys.exit(0)

    if cur * 2 <= B:
        dq.append((cur*2, num + 1))

    n = int(str(cur) + '1')
    if n <= B:
        dq.append((n, num + 1))

print(-1)


