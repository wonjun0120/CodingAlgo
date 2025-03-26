import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()

i = 0
count = 0
answer = 0

while i < m - 2:
    if s[i] == 'I' and s[i + 1] == 'O' and s[i + 2] == 'I':
        count += 1
        if count == n:
            answer += 1
            count -= 1  
        i += 2  
    else:
        count = 0
        i += 1

print(answer)
