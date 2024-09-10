import sys

input = sys.stdin.readline
n, m = map(int, input().split())
cards = list(map(int, input().split()))

cards.sort()

max_ans = 0
for i in range(n - 2):
    left, right = i + 1, n - 1

    while left < right:
        tot = cards[i] + cards[left] + cards[right]

        if tot == m:
            print(tot)
            sys.exit(0)
        elif tot < m:
            max_ans = max(max_ans, tot)
            left += 1
        else:
            right -= 1

print(max_ans)
