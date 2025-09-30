def find_2b2(m, n, board):
    answer = []
    for i in range(m):
        for j in range(n):
            cur = board[i][j]
            if cur == '': continue
            
            cnt = 0
            for dx, dy in [(1, 0), (0, 1), (1, 1)]:
                nx = i + dx
                ny = j + dy
                if nx < m and ny < n and board[nx][ny] == cur:
                    cnt += 1
                else:
                    break
            if cnt == 3:
                answer.append((i, j))
                    
    return answer

def pop_board(to_pop, board):
    for x, y in to_pop:
        for dx, dy in [(0, 0), (1, 0), (0, 1), (1, 1)]:
            nx, ny = x + dx, y + dy
            board[nx][ny] = ''
    return board

def down_board(m, n, board):
    for y in range(n):
        write = m - 1
        for x in range(m - 1, -1, -1):
            if board[x][y] != '':
                board[write][y] = board[x][y]
                write -= 1
        for x in range(write, -1, -1):
            board[x][y] = ''
    return board

def solution(m, n, board):
    board = [list(row) for row in board]
    
    to_pop = find_2b2(m, n, board)

    while to_pop:
        board = pop_board(to_pop, board)
        board = down_board(m, n, board)
        to_pop = find_2b2(m, n, board)
        
    answer = 0
    
    for x in range(m):
        for y in range(n):
            if board[x][y] == '': 
                answer += 1
    return answer