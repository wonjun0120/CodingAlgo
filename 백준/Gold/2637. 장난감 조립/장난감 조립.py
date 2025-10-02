import sys
from collections import deque

input = sys.stdin.readline

N = int(input().strip())          
M = int(input().strip())

adj = [[] for _ in range(N + 1)]
indeg = [0] * (N + 1)

for _ in range(M):
    t, prod, cnt = map(int, input().split())
    adj[prod].append((t, cnt))
    indeg[t] += 1

dp = [[0] * (N + 1) for _ in range(N + 1)]

q = deque()
for i in range(1, N + 1):
    if indeg[i] == 0:
        dp[i][i] = 1
        q.append(i)

while q:
    cur = q.popleft()
    for nxt, need in adj[cur]:
        for b in range(1, N + 1):
            if dp[cur][b]:
                dp[nxt][b] += dp[cur][b] * need
        indeg[nxt] -= 1
        if indeg[nxt] == 0:
            q.append(nxt)

for b in range(1, N + 1):
    if dp[N][b] > 0:
        print(b, dp[N][b])
