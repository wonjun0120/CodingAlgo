import sys

input = sys.stdin.readline

t = int(input().strip())
p = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]

for _ in range(t):
    n = int(input().strip())

    if n < len(p):
        print(p[n - 1])

    else:
        for i in range(len(p), n):
            p.append(p[i - 1] + p[i - 5])

        print(p[n - 1])
    