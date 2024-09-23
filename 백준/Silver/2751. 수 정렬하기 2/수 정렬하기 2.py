import sys
input = sys.stdin.readline

n = int(input())

li = []
for _ in range(n):
    li.append(int(input()))

li.sort()

for el in li:
    print(el)