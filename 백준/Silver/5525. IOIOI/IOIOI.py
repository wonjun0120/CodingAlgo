import sys
import collections

input = sys.stdin.readline

n = int(input())
m = int(input())
s = list(input().strip())

ioi = "I"
for _ in range(n):
    ioi += "OI"

answer = 0
for i in range(m):
    if s[i] == "I":
        if (i + len(ioi)) <= m:
            answer += 1
            for j in range(len(ioi)):
                if s[i + j] != ioi[j]:
                    answer -= 1
                    break

print(answer)
