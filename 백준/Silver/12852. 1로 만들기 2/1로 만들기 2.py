import sys

input = sys.stdin.readline
n = int(input())

paths = [[], [1], [2, 1], [3, 1]]
dp = [0 for _ in range(n + 1)]
if n > 1: dp[2] = 1
if n > 2: dp[3] = 1

for i in range(4, n + 1):
    min_case = dp[i - 1]
    path = i - 1
    if i % 2 == 0:
        if min_case > dp[i // 2]:
            path = i // 2
            min_case = dp[i // 2]
    if i % 3 == 0:
        if min_case > dp[i // 3]:
            path = i // 3
            min_case = dp[i // 3]

    dp[i] = min_case + 1
    paths.append([i] + paths[path])

print(dp[n])
print(' '.join([str(x) for x in paths[n]]))
