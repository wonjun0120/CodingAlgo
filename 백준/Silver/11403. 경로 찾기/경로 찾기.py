import sys
import collections

input = sys.stdin.readline
n = int(input())

graph_li = [list(map(int, input().strip().split())) for _ in range(n)]
graph = {k : [] for k in range(n)}
for i in range(n):
    for j in range(n):
        if graph_li[i][j] == 1:
            graph[i].append(j)

answer = []
for i in range(n):
    stack = collections.deque(graph[i])
    # print(i, graph_li)
    # print(stack)
    tmp = [0] * n
    while stack:
        cur = stack.pop()
        if tmp[cur] == 1:
            continue
        
        if tmp[cur] == 0:
            tmp[cur] = 1
            for it in graph[cur]:
                stack.append(it)
    answer.append(tmp)


for li in answer:
    print(" ".join([str(n) for n in li]))
