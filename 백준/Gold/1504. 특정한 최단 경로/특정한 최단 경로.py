import sys
import heapq

input = sys.stdin.readline
INF = 10**18

N, E = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

def dijkstra(start: int) -> list:
    dist = [INF] * (N + 1)
    dist[start] = 0
    pq = [(0, start)]
    while pq:
        d, x = heapq.heappop(pq)
        if d > dist[x]:
            continue
        for nx, w in graph[x]:
            nd = d + w
            if nd < dist[nx]:
                dist[nx] = nd
                heapq.heappush(pq, (nd, nx))
    return dist

dist1 = dijkstra(1)
dist_v1 = dijkstra(v1)
dist_v2 = dijkstra(v2)

path1 = dist1[v1] + dist_v1[v2] + dist_v2[N]  # 1 -> v1 -> v2 -> N
path2 = dist1[v2] + dist_v2[v1] + dist_v1[N]  # 1 -> v2 -> v1 -> N

ans = min(path1, path2)
print(ans if ans < INF else -1)
