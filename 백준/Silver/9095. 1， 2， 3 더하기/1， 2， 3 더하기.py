import sys

input = sys.stdin.readline
n = int(input())
dp = [0, 1, 2, 4]

for _ in range(n):
    tc = int(input())

    if len(dp) - 1 >= tc:
        print(dp[tc])
        continue

    for i in range(len(dp), tc + 1):
        dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])
    print(dp[tc])
