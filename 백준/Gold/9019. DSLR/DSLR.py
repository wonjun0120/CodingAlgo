import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [False] * 10000
    queue = deque()
    queue.append((A, ""))
    visited[A] = True

    while queue:
        n, c = queue.popleft()

        # D
        d = (n * 2) % 10000
        if not visited[d]:
            if d == B:
                print(c + 'D')
                break
            visited[d] = True
            queue.append((d, c + 'D'))

        # S
        s = 9999 if n == 0 else n - 1
        if not visited[s]:
            if s == B:
                print(c + 'S')
                break
            visited[s] = True
            queue.append((s, c + 'S'))

        # L
        l = (n % 1000) * 10 + (n // 1000)
        if not visited[l]:
            if l == B:
                print(c + 'L')
                break
            visited[l] = True
            queue.append((l, c + 'L'))

        # R
        r = (n % 10) * 1000 + (n // 10)
        if not visited[r]:
            if r == B:
                print(c + 'R')
                break
            visited[r] = True
            queue.append((r, c + 'R'))
