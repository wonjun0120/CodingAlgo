import sys

input = sys.stdin.readline

n, m = map(int, input().split())

campus = []
x, y = 0, 0
for i in range(n):
    li = input().strip()
    campus.append(li)
    for j, el in enumerate(li):
        if el == 'I':
            x, y = i, j

stack = [(x, y)]

is_visit = [[False for _ in range(m)] for _ in range(n)]
answer = 0
while len(stack) > 0:
    x, y = stack.pop()
    if x < 0 or x >= n:
        continue

    if y < 0 or y >= m:
        continue

    if is_visit[x][y]:
        continue

    is_visit[x][y] = True

    if campus[x][y] == 'X':
        continue

    if campus[x][y] == 'P':
        answer += 1

    stack.append((x - 1, y))
    stack.append((x + 1, y))
    stack.append((x, y - 1))
    stack.append((x, y + 1))

if answer == 0:
    print('TT')
else:
    print(answer)