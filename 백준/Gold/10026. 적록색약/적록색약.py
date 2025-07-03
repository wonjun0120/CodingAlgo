import sys
from collections import deque

input = sys.stdin.readline

def bfs(sx, sy, graph, is_visited):

    dq = deque([(sx, sy)])
    while dq:
        x, y = dq.popleft()
        color = graph[x][y]
        is_visited[x][y] = True

        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N:
                if not is_visited[nx][ny] and graph[nx][ny] == color:
                    is_visited[nx][ny] = True
                    dq.append((nx, ny))

def cnt_area(graph):
    is_visited = [[0] * N for _ in range(N)]
    area_num = 0

    for x in range(N):
        for y in range(N):
            if not is_visited[x][y]:
                area_num += 1
                bfs(x, y, graph, is_visited)

    return area_num


N = int(input())
origin_display = [list(input().strip()) for _ in range(N)]
origin_display_area = cnt_area(origin_display)

for i, row in enumerate(origin_display):
    for j, el in enumerate(row):
        if el == 'R': 
            origin_display[i][j] = 'G'
colorless_display_area = cnt_area(origin_display)

print(origin_display_area, colorless_display_area)


