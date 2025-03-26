import sys
import collections

input = sys.stdin.readline
n = int(input())

def find(i, j):
    queue = collections.deque()
    queue.append((i, j))
    count = 0

    while queue:
        a, b = queue.popleft()
        if field[a][b] == 1:
            count += 1
            field[a][b] = -1

            for dx, dy in [(1,0), (0,1), (-1,0), (0,-1)]:
                na, nb = a + dx, b + dy
                if 0 <= na < n and 0 <= nb < n and field[na][nb] == 1:
                    queue.append((na, nb))
    return count

field = [list(map(int, input().strip())) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(n):
        if field[i][j] == 1:
            size = find(i, j)
            answer.append(size)

answer.sort()
print(len(answer))
for num in answer:
    print(num)
