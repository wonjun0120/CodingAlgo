import sys
import math

input = sys.stdin.readline

n = int(input())
for _ in range(n):
    M, N, x, y = map(int, input().strip().split())
    mnlcm = math.lcm(M, N)

    answer = -1
    k = 0
    year = (k * M) + x
    while year <= mnlcm:
        # print(year, N, year % N, y)
        if year % N == y % N:
            answer = year
            break
        k += 1
        year = (k * M) + x

    print(answer)