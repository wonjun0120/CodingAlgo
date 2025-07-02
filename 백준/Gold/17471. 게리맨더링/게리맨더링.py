import sys
import collections

input = sys.stdin.readline

N = int(input())
population = {i + 1: x for i, x in enumerate(map(int, input().strip().split()))}
graph = {}
for i in range(N):
    graph[i + 1] = list(map(int, input().strip().split()))[1:]

def is_in_line(graph, ext):
    if len(ext) <= 1: return True

    start = ext[0]
    visited = {start}
    dq = collections.deque([start])

    while dq:
        v = dq.popleft()
        for nv in graph[v]:
            if nv in ext and nv not in visited:
                visited.add(nv)
                dq.append(nv)

    return visited == set(ext)


li = set(range(1, N + 1))
dq = collections.deque(([[x] for x in range(N, 0,-1)]))
cases = set()
answer = -1
while dq:
    cur = dq.pop()
    key_cur = frozenset(cur)
    if key_cur in cases:
        continue

    ext = list(li - set(cur))
    key_ext = frozenset(ext)

    if is_in_line(graph, cur) and is_in_line(graph, ext):
        vote1 = sum(population[x] for x in cur)
        vote2 = sum(population[x] for x in ext)
        diff = abs(vote1 - vote2)
        answer = diff if answer == -1 else min(answer, diff)

    cases.add(key_cur)
    cases.add(key_ext)

    for v in cur:
        for n in graph[v]:
            if n in key_cur: continue
            dq.append((sorted(cur + [n])))

print(answer)
