import sys
import heapq

input = sys.stdin.readline

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v, cost = map(int, input().strip().split())
    graph[u].append((v, cost))

start, end = map(int, input().strip().split())

INF = float('inf')
min_cost = [INF] * (N + 1)
min_cost[start] = 0

hq = [(0, start)]

while hq:
    cur_cost, cur_city = heapq.heappop(hq)

    if min_cost[cur_city] < cur_cost:
        continue

    for next_city, cost in graph[cur_city]:
        new_cost = cur_cost + cost
        if new_cost < min_cost[next_city]:
            min_cost[next_city] = new_cost
            heapq.heappush(hq, (new_cost, next_city))

print(min_cost[end])
