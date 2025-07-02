import sys
import collections

input = sys.stdin.readline

N, M = map(int, input().strip().split())

lab_map = []
empty_loc = []
virus_loc = []
for i in range(N):
    li = list(map(int, input().strip().split()))
    lab_map.append(li)
    for j, el in enumerate(li):
        if el == 0: empty_loc.append((i, j))
        if el == 2: virus_loc.append((i, j))

def spread_virus(lab_map, virus_loc):
    dq = collections.deque(virus_loc)

    while dq:
        x, y = dq.pop()
        for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and lab_map[nx][ny] == 0:
                lab_map[nx][ny] = 2
                dq.append((nx, ny))

    return sum([row.count(0) for row in lab_map])

max_size = 0
def dfs(lab_map, empty_loc, idx, cnt):
    global max_size
    if cnt == 3:
        max_size = max(max_size, spread_virus([r[:] for r in lab_map], virus_loc))
        return

    for i in range(idx, len(empty_loc)):
        x, y = empty_loc[i]
        lab_map[x][y] = 1
        dfs(lab_map, empty_loc, i + 1, cnt + 1)
        lab_map[x][y] = 0

dfs(lab_map,empty_loc,0,0)
print(max_size)
