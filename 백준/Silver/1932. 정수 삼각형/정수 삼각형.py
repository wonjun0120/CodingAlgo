import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
triangle = []
for _ in range(N):
    row = list(map(int, input().strip().split()))
    triangle.append(row)

if N == 1:
    print(triangle[0][0])
    sys.exit(0)

update = []
for i in range(N - 1, 0, -1):
    row = triangle[i]
    if len(update) > 0:
        row = [row[i] + update[i] for i in range(len(row))]
    update = [max(row[i - 1], row[i]) for i in range(1, len(row))]

print(triangle[0][0] + update[0])
