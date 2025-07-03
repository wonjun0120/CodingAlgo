import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().strip().split())
area = [list(map(int, input().strip().split())) for _ in range(N)]
max_num = 0

"""

0-0-0 - 
| | |

"""

def recur(x, y, path, cnt, sums):
    global max_num
    if cnt == 3:
        m = 0
        for x, y in path:
            for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M:
                    if (nx, ny) not in path:
                        m = max(m, area[nx][ny])
        max_num = max(max_num, m + sums)
        return

    for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M:
            if (nx, ny) in path: continue
            recur(nx, ny, path + [(nx, ny)], cnt + 1, sums + area[nx][ny])
            

for x in range(N):
    for y in range(M):
        recur(x,y,[(x,y)], 1, area[x][y])

print(max_num)
