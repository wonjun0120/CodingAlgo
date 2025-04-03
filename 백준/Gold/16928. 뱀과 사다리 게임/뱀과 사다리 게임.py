import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
game_map = {}

for _ in range(N + M):
    x, y = map(int, input().split())
    game_map[x] = y

queue = deque([(1, 0)])
visited = [False] * 101
visited[1] = True

while queue:
    cur, time = queue.popleft()

    for i in range(1, 7):
        nxt = cur + i
        if nxt > 100:
            continue
        move = game_map.get(nxt, nxt)

        if not visited[move]:
            if move == 100:
                print(time + 1)
                sys.exit(0)
            visited[move] = True
            queue.append((move, time + 1))
