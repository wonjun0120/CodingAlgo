import sys
from collections import deque

input = sys.stdin.readline

M, N = map(int, input().split())  # 열, 행

store = []
queue = deque()
unripe_count = 0

for n in range(N):
    row = list(map(int, input().split()))
    for m, val in enumerate(row):
        if val == 1:
            queue.append((n, m, 0))  # (행, 열, 시간)
        elif val == 0:
            unripe_count += 1
    store.append(row)

# 모든 토마토가 익어있다면
if unripe_count == 0:
    print(0)
    sys.exit(0)

answer = 0
dn = [1, -1, 0, 0]
dm = [0, 0, 1, -1]

while queue:
    cn, cm, time = queue.popleft()
    for i in range(4):
        nn, nm = cn + dn[i], cm + dm[i]
        if 0 <= nn < N and 0 <= nm < M:
            if store[nn][nm] == 0:
                store[nn][nm] = 1
                unripe_count -= 1
                queue.append((nn, nm, time + 1))
                answer = max(answer, time + 1)

# 다 익지 못한 토마토가 있다면
if unripe_count > 0:
    print(-1)
else:
    print(answer)
