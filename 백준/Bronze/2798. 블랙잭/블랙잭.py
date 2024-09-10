import sys

input = sys.stdin.readline
n, m = [int(x) for x in input().split(' ')]
cards = [int(x) for x in input().split(' ')]

cards.sort(reverse=True)
flag = False
max_ans = 0

for i in range(len(cards)):
    if flag: break
    for j in range(i + 1, len(cards)):
        if flag: break
        for k in range(j + 1, len(cards)):
            answer = cards[i] + cards[j] + cards[k]
            if answer == m:
                max_ans = answer
                flag = True
                break
            elif answer < m:
                max_ans = max(answer, max_ans)

print(max_ans)