import sys
input = sys.stdin.readline

def need_paint(cut_board):
    b_board = [
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB"
    ]
    w_board = [
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW",
        "WBWBWBWB",
        "BWBWBWBW"
    ]

    b_cnt = 0
    w_cnt = 0
    for i in range(len(cut_board)):
        for j in range(len(cut_board[0])):
            if b_board[i][j] != cut_board[i][j]: b_cnt += 1
            if w_board[i][j] != cut_board[i][j]: w_cnt += 1

    return min(b_cnt, w_cnt)

n, m = [int(x) for x in input().strip().split()]
board = []
for _ in range(n):
    board.append(input().strip())
min_paint = n * m

for i in range(n - 7):
    for j in range(m - 7):
        cut_board = [b[j : j + 8] for b in board[i : i + 8]]
        min_paint = min(min_paint, need_paint(cut_board))

print(min_paint)