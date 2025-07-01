import sys
from itertools import product

input = sys.stdin.readline

answers = list(map(int, input().strip().split()))
N = 10
result = 0

for ans in product(range(1, 6), repeat=10):
    is_break = False
    for i in range(2, N):
        if ans[i] == ans[i - 1] == ans[i - 2]:
            is_break = True
            break

    if is_break: continue

    score = sum(a == b for a, b in zip(ans, answers))
    if score >= 5:
        result += 1

print(result)
