import sys
from collections import deque
from copy import deepcopy

input = sys.stdin.readline

def bfs(display, visited, N):
    count = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                count += 1
                color = display[i][j]
                queue = deque([(i, j)])
                visited[i][j] = 1
                while queue:
                    x, y = queue.popleft()
                    for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                        nx, ny = x + dx, y + dy
                        if 0 <= nx < N and 0 <= ny < N:
                            if visited[nx][ny] == 0 and display[nx][ny] == color:
                                visited[nx][ny] = 1
                                queue.append((nx, ny))
    return count

N = int(input())
display = [list(input().strip()) for _ in range(N)]

visited_normal = [[0]*N for _ in range(N)]
normal_count = bfs(display, visited_normal, N)

display_rg = deepcopy(display)
for i in range(N):
    for j in range(N):
        if display_rg[i][j] == 'R':
            display_rg[i][j] = 'G'

visited_rg = [[0]*N for _ in range(N)]
rg_count = bfs(display_rg, visited_rg, N)

print(normal_count, rg_count)
