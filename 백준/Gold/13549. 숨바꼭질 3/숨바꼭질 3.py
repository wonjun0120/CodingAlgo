import sys
import collections

input = sys.stdin.readline

N, K = map(int, input().split())

MAX = max(K, N) + 6
visited = [False] * (MAX + 1)
dq = collections.deque([(N, 0)])
visited[N] = True

while dq:
    x, t = dq.popleft()
    if x == K:
        print(t)
        break
    
    nx = x * 2
    if 0 <= nx <= MAX and not visited[nx]:
        visited[nx] = True
        dq.appendleft((nx, t))

    for nx in (x - 1, x + 1):
        if 0 <= nx <= MAX and not visited[nx]:
            visited[nx] = True
            dq.append((nx, t + 1))
