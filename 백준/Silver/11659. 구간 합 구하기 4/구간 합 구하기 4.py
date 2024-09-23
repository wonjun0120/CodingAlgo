import sys

input = sys.stdin.readline
n, m = [int(x) for x in input().split()]
nums = [int(x) for x in input().split()]
dp = [0]

prev = 0
for el in nums:
    prev += el
    dp.append(prev)

for _ in range(m):
    i, j = [int(x) for x in input().split()]
    print(dp[j] - dp[i - 1])