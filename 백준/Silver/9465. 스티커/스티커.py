import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    stickers = [list(map(int, input().split())) for _ in range(2)]
    
    if n == 1:
        print(max(stickers[0][0], stickers[1][0]))
        continue

    dp = [[0] * 2 for _ in range(n)]
    
    dp[0][0] = stickers[0][0]
    dp[0][1] = stickers[1][0]
    
    for i in range(1, n):
        dp[i][0] = max(dp[i-1][1], dp[i-2][1] if i > 1 else 0) + stickers[0][i]
        dp[i][1] = max(dp[i-1][0], dp[i-2][0] if i > 1 else 0) + stickers[1][i]

    print(max(dp[n-1][0], dp[n-1][1]))
