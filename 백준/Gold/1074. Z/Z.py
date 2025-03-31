import sys
import collections

input = sys.stdin.readline

N, r, c = map(int, input().split())

max_n = 2**N * 2**N - 1

lr, rr, lc, rc = 0, 2**N - 1, 0, 2**N - 1 
li = collections.deque([])

answer = 0

for i in range(N):
    mr = int((lr + rr) / 2)
    mc = int((lc + rc) / 2)
    # print(lr, rr, lc, rc, mr, mc)
    base = 2 **(2*(N-1-i))
    if r <= mr and c <= mc: # 0
        li.append(0)
        base *= 0
        rr = mr
        rc = mc

    if r <= mr and c > mc: # 1
        li.append(1)
        base *= 1
        rr = mr
        lc = mc + 1

    if r > mr and c <= mc: # 2
        li.append(2)
        base *= 2
        lr = mr + 1
        rc = mc

    if r > mr and c > mc: # 3
        li.append(3)
        base *= 3
        lr = mr + 1
        lc = mc + 1

    answer += base

print(answer)


