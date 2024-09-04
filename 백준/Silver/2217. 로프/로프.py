import sys
input = sys.stdin.readline

n = int(input())

ropes = []
for _ in range(n):
    ropes.append(int(input()))

ropes.sort(reverse=True)

max_weight = 0
for i, rope in enumerate(ropes):
    max_weight = max(max_weight, rope * (i + 1))

print(max_weight)