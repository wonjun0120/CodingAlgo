import sys
from collections import deque

input = sys.stdin.readline

ISBN = list(input().strip())

m = 0
idx = -1
for i, num in enumerate(ISBN):
    print
    if num == "*":
        idx = i
    else:     
        if i % 2 == 0:
            m += int(num)
        
        else:
            m += (int(num) * 3)

mul = 1
if idx % 2 == 1:
    mul = 3

for i in range(10):
    tmp = m + (i * mul)
    if tmp % 10 == 0:
        print(i)


