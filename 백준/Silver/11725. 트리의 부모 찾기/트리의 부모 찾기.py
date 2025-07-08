import sys
from collections import deque

input = sys.stdin.readline

def find_parent(graph):   
    visited = [0] * (N + 1)
    visited[1] = 1

    dq = deque([1])
    while dq:
        cur = dq.popleft()
        child = graph[cur]

        for el in child:
            if visited[el] == 0:
                visited[el] = cur
                dq.append(el)
    return visited



N = int(input())
graph = {}
for _ in range(N - 1):
    x, y = map(int, input().strip().split())
    graph.setdefault(x, set()).add(y)
    graph.setdefault(y, set()).add(x)

res = find_parent(graph)
# print(res)
for node in range(2, N + 1):
    print(res[node])

