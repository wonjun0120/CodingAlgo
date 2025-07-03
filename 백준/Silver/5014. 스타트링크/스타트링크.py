import sys
from collections import deque

input = sys.stdin.readline

F, S, G, U, D = map(int, input().strip().split()) 

is_visit = [0] * (F + 1)
is_visit[S] = 1
dq = deque([(S, 0)])

while dq:
    cur_floor, time = dq.popleft()
    
    if cur_floor == G:
        print(time)
        sys.exit(0)

    for df in [U, -D]:
        nf = cur_floor + df
        if 1 <= nf <= F:
            if is_visit[nf] == 0:
                is_visit[nf] = 1
                dq.append((nf, time + 1))


print("use the stairs")
