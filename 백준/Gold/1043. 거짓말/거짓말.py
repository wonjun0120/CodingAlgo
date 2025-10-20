import sys
input = sys.stdin.readline

def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]
        x = parent[x]
    return x

def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return
    parent[rb] = ra

N, M = map(int, input().split())
data = list(map(int, input().split()))
T = data[0]
truth = data[1:] if T > 0 else []

parties = []
for _ in range(M):
    arr = list(map(int, input().split()))
    cnt, people = arr[0], arr[1:]
    parties.append(people)

if T == 0:
    print(M)
    sys.exit(0)

parent = [i for i in range(N + 1)]

for people in parties:
    for i in range(1, len(people)):
        union(people[0], people[i])

truth_roots = {find(x) for x in truth}

answer = 0
for people in parties:
    if all(find(p) not in truth_roots for p in people):
        answer += 1

print(answer)
