import sys

input = sys.stdin.readline
n = int(input())

dp = [0, 1, 3]

if n < len(dp):
    answer = dp[n]
    print(answer % 10007)

else:
    for i in range(len(dp), n + 1):
        tmp = 0
        # 마지막 1 * 2
        tmp += dp[i - 1]

        # 마지막 2 * 1
        tmp += dp[i - 2]

        # 마지막 2 * 2
        tmp += dp[i - 2]
        dp.append(tmp)

    answer = dp[n]
    print(answer % 10007)