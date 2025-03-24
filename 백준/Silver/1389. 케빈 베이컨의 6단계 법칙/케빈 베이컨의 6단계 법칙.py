import sys

input = sys.stdin.readline

n, m = map(int, input().split())

graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph.setdefault(a, set()).add(b)
    graph.setdefault(b, set()).add(a)

# print(graph)
min_num = float('inf')
answer = 0
for a in range(1, n + 1):
    is_visit = [0] * (n + 1)
    queue = [a]
    # print("a -> ", a)
    while queue:
        cur = queue.pop(0)
        # print("is_visit", is_visit)
        # print("cur -> ", cur)
        for el in graph[cur]:
            if is_visit[el] != 0 or el == a:
                continue
            is_visit[el] = is_visit[cur] + 1
            queue.append(el)
    
    if sum(is_visit) < min_num :
        answer = a
        min_num = sum(is_visit)

print(answer)