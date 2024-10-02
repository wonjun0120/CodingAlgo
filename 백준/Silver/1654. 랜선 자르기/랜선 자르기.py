import sys

input = sys.stdin.readline

k, n = [int(x) for x in input().strip().split()]

lengths = []
for _ in range(k):
    length = int(input())
    lengths.append(length)

l = 1
r = max(lengths)
while True:
    if l > r:
        break

    m = (l + r) // 2
    ans = sum([x // m for x in lengths])
    if ans >= n:
        l = m + 1
    else:
        r = m - 1

print(r)