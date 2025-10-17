import sys

input = sys.stdin.readline

N = int(input().strip())
board = [[1] * (N + 1)]
for _ in range(N):
    board.append([1] + list(map(int, input().split())))

dp = [[[0] * 3 for _ in range(N + 1)] for _ in range(N + 1)]

if board[1][2] == 0:
    dp[1][2][0] = 1

for r in range(1, N + 1):
    for c in range(1, N + 1):
        if board[r][c] == 1:
            continue

        if dp[r][c][0]:
            if c + 1 <= N and board[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][0]
            if r + 1 <= N and c + 1 <= N:
                if board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
                    dp[r + 1][c + 1][2] += dp[r][c][0]

        if dp[r][c][1]:
            if r + 1 <= N and board[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][1]
            if r + 1 <= N and c + 1 <= N:
                if board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
                    dp[r + 1][c + 1][2] += dp[r][c][1]

        if dp[r][c][2]:
            if c + 1 <= N and board[r][c + 1] == 0:
                dp[r][c + 1][0] += dp[r][c][2]
            if r + 1 <= N and board[r + 1][c] == 0:
                dp[r + 1][c][1] += dp[r][c][2]
            if r + 1 <= N and c + 1 <= N:
                if board[r][c + 1] == 0 and board[r + 1][c] == 0 and board[r + 1][c + 1] == 0:
                    dp[r + 1][c + 1][2] += dp[r][c][2]

print(sum(dp[N][N]))
