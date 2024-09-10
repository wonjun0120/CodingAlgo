import sys

input = sys.stdin.readline
n = int(input())

answer = 0
acc = 0
while True:
    acc += answer
    answer += 1
    if (6 * acc) + 1 >=  n:
        break 
    
print(answer)

