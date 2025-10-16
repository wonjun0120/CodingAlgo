import sys
from itertools import combinations

input = sys.stdin.readline

N, M = map(int, input().split())
houses, shops = [], []
for i in range(N):
    row = list(map(int, input().split()))
    for j, v in enumerate(row):
        if v == 1:
            houses.append((i, j))
        elif v == 2:
            shops.append((i, j))

H, S = len(houses), len(shops)

dist = [[0]*S for _ in range(H)]
for hi, (hx, hy) in enumerate(houses):
    for si, (sx, sy) in enumerate(shops):
        dist[hi][si] = abs(hx - sx) + abs(hy - sy)

ans = float('inf')

for comb in combinations(range(S), M):
    total = 0
    for hi in range(H):
        mn = min(dist[hi][si] for si in comb)
        total += mn
        if total >= ans:
            break
    if total < ans:
        ans = total

print(ans)
