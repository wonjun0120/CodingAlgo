import sys
import collections

input = sys.stdin.readline

n, m = map(int, input().split())
maze = []

for _ in range(n):
    maze.append(list(map(int, list(input())[:-1])))

deque = collections.deque()
deque.append((0, 0, 1))
is_visit = [[-1] * m for _ in range(n)]
while deque:
    x, y, time = deque.popleft()

    if x == n - 1 and y == m - 1:
        print(time)
        break

    for a, b in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= x + a and x + a < n and 0 <= y + b and y + b < m:
            if maze[x+a][y+b] == 1 and is_visit[x+a][y+b] == -1:
                is_visit[x+a][y+b] = 1
                deque.append((x+a,y+b,time+1))


