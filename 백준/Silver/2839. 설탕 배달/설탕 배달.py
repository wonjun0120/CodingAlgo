import sys

input = sys.stdin.readline

n = int(input())

answer = -1
for i in range(n // 5 + 1):
    if i == 0:
        if n % 3 == 0:
            answer = n // 3
        continue

    if (n - (5 * i)) % 3 != 0:
        continue
    num3 = (n - (5 * i)) // 3
    if answer == -1:
        answer = num3 + i
    answer = min(answer, num3 + i)

print(answer)