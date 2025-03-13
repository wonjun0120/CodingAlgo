import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = {i: [] for i in range(1, n + 1)}
is_visited = [False] * (n + 1)  

def dfs(node):
    stack = [node]
    while stack:
        current = stack.pop()
        if not is_visited[current]:
            is_visited[current] = True
            stack.extend(graph[current])

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

answer = 0
for node in range(1, n + 1):
    if not is_visited[node]: 
        dfs(node)
        answer += 1

print(answer)
