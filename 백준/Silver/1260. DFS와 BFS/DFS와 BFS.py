import sys
input = sys.stdin.readline

n, m, v = [int(x) for x in input().strip().split()]

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = [int(x) for x in input().strip().split()]
    graph[a].append(b)
    graph[b].append(a)


def dfs(graph, start):
    visited, stack = [], [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack += sorted(graph[node], reverse=True)
    return visited

def bfs (graph, start):
    visited, queue = [], [start]

    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            queue += sorted(graph[node])
    return visited

print(" ".join([str(x) for x in dfs(graph, v)]))
print(" ".join([str(x) for x in bfs(graph, v)]))
