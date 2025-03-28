import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())  

mapp = []
start_x, start_y = -1, -1  

for i in range(n):
    row = list(map(int, input().split()))
    if start_x == -1:  
        for j in range(m):
            if row[j] == 2:
                start_x, start_y = i, j
    mapp.append(row)

answer = [[-1] * m for _ in range(n)]

visited = [[False] * m for _ in range(n)]

queue = collections.deque()
queue.append((start_x, start_y))
visited[start_x][start_y] = True
answer[start_x][start_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue.popleft()

    for dir in range(4):
        nx = x + dx[dir]
        ny = y + dy[dir]

        if 0 <= nx < n and 0 <= ny < m:
            if not visited[nx][ny] and mapp[nx][ny] == 1:
                visited[nx][ny] = True
                answer[nx][ny] = answer[x][y] + 1
                queue.append((nx, ny))

for i in range(n):
    row_result = []
    for j in range(m):
        if mapp[i][j] == 0:
            row_result.append("0")
        else:
            row_result.append(str(answer[i][j]))
    print(" ".join(row_result))
