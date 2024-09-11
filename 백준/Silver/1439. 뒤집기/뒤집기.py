import sys

input = sys.stdin.readline
n = input().strip()

zero = 0
one = 0
last = n[0]
for i in range(len(n) - 1):
    cur = n[i + 1]
    if last != cur:
        if last == "0": zero += 1
        else : one += 1
        last = cur
    if i + 1 == len(n) - 1:
        if last == cur:
            if last == "0": zero += 1
            else : one += 1
        else:
            zero += 1
            one += 1
            
print(min(zero, one))