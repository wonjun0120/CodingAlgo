import sys

input = sys.stdin.readline

N, K = map(int, input().split())
items = [tuple(map(int, input().split())) for _ in range(N)]

dp = [0] * (K + 1)
for W, V in items:
    for w in range(K, W - 1, -1):
        if dp[w - W] + V > dp[w]:
            dp[w] = dp[w - W] + V

print(max(dp))
