import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append([x for x in input().strip().split()])

li.sort(key=lambda x : int(x[0]))

for el in li:
    print(' '.join(el))