import sys

input = sys.stdin.readline
n = int(input())

dp = [0, 1, 2, 3, 1]

for i in range(len(dp), n + 1):
    dp.append(1 + min(dp[i - j * j] for j in range(1, int(i ** 0.5) + 1)))

print(dp[n])