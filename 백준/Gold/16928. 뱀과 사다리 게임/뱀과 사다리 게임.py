import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
game_map = {}

for _ in range(N):
    x, y = map(int, input().split())
    game_map.setdefault(x, []).append(y)


for _ in range(M):
    u, v = map(int, input().split())
    game_map.setdefault(u, []).append(v)

stack = deque([(1, 0)])
is_visit= [False] * 101
is_visit[1] = True
# print(game_map)
while stack:
    cur, time = stack.popleft()
    # print(cur, time)
    to_move = cur
    for i in range(1, 7):
        if cur + i > 100: continue
        if not is_visit[cur + i]:
            if cur + i == 100:
                print(time + 1)
                sys.exit(0)

            if cur + i in game_map.keys():
                for mv in game_map[cur + i]:
                    stack.append((mv, time + 1))
            else:
                to_move = max(cur + i, to_move)
            is_visit[cur + i] = True
    
    stack.append((to_move, time + 1))
