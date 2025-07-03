import sys
from collections import deque

input = sys.stdin.readline

def melt(i, j, cheese):
    is_visited = [[0] * M for _ in range(N)]
    is_visited[i][j] = 1

    dq = deque([(i, j)])
    cheese_cnt = 0
    while dq:
        x, y = dq.popleft()
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < M:
                if is_visited[nx][ny] == 0:
                    is_visited[nx][ny] = 1
                    cur = cheese[nx][ny]
                    if cur == 0:
                        dq.append((nx, ny))
                    else:
                        cheese_cnt += 1
                        cheese[nx][ny] = 0

    return cheese_cnt


N, M = map(int, input().strip().split())
cheese = [list(map(int, input().strip().split())) for _ in range(N)]

# print()
# print()
# [print(''.join(str(r))) for r in cheese]
# melt(0,0,cheese)
# print()
# [print(''.join(str(r))) for r in cheese]

cnt = 0
cheese_cnt = 0
for i in range(N):
    for j in range(M):
        if (i == 0 and j == 0) or cheese[i][j] == 1:
            cnt += 1
            cheese_cnt = melt(i, j, cheese)

print(cnt)
print(cheese_cnt)
