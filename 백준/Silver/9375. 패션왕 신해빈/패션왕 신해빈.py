import sys

input = sys.stdin.readline

t = int(input().strip())

for _ in range(t):
    n = int(input().strip())

    clothes = {}
    for _ in range(n):
        name, kind = input().strip().split()

        if kind in clothes:
            clothes[kind] += 1
        else:
            clothes[kind] = 1

    tmp = [x + 1 for x in clothes.values()]

    result = 1
    for x in tmp:
        result *= x


    print(result - 1)
