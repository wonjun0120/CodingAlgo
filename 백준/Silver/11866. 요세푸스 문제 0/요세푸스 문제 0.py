import sys

input = sys.stdin.readline

n, k = [int(x) for x in input().strip().split()]

li = [x for x in range(1, n + 1)]
answer = []
idx = 0
while True:
    if len(answer) >= n:
        break
    if len(li) < 1:
        break

    idx = (idx + k - 1) % len(li)
    answer.append(str(li.pop(idx)))


print("<" + ", ".join(answer) + ">")
