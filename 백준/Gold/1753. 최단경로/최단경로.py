import sys
import heapq

input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

INF = float('inf')
dist = [INF] * (V + 1)
dist[K] = 0

hq = [(0, K)]
while hq:
    d, u = heapq.heappop(hq)
    if d > dist[u]:
        continue
    for w, v in adj[u]:
        nd = d + w
        if nd < dist[v]:
            dist[v] = nd
            heapq.heappush(hq, (nd, v))

out = []
for i in range(1, V + 1):
    if dist[i] == INF:
        out.append("INF")
    else:
        out.append(str(dist[i]))
sys.stdout.write("\n".join(out))
