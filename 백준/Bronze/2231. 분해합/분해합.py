import sys

input = sys.stdin.readline
n = int(input())

flag = True
for i in range(n):
    tmp = i + sum([int(x) for x in str(i)])
    if tmp == n:
        flag = False
        print(i)
        break

if flag:
    print(0)