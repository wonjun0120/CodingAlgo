import sys

input = sys.stdin.readline

c = int(input().strip())
n = int(input().strip())

computers = [[] for _ in range(c + 1)]
for _ in range(n):
    x, y = [int(x) for x in input().strip().split()]

    computers[x].append(y)
    computers[y].append(x)

stack = [1]
virus = []
while len(stack) > 0:
    cur = stack.pop()
    virus.append(cur)
    stack += computers[cur]
    computers[cur] = []

print(len(set(virus)) - 1)