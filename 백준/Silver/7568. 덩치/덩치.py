import sys
input = sys.stdin.readline

n = int(input())
li = []
for _ in range(n):
    x, y = [int(x) for x in input().strip().split()]
    li.append((x, y))

answers = []
for el in li:
    cnt = 1
    for cmp in li:
        if cmp[0] > el[0] and cmp[1] > el[1]:
            cnt += 1

    answers.append(str(cnt))

print(" ".join(answers))