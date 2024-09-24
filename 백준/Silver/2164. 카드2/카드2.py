import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
queue = deque([i for i in range(1, n + 1)])

flag = False
while True:
    if len(queue) <= 1:
        print(queue[0])
        break
    tmp = queue.popleft()
    if flag:
        queue.append(tmp)
    flag = not flag
