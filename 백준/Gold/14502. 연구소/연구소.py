import sys
import itertools
import collections
import copy

input = sys.stdin.readline

def spread_virus(lab_map, virus):
    stack = collections.deque(virus)

    while stack:
        i, j = stack.pop()
        for x, y in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
            if 0 <= i + x < N and 0 <= j + y < M:
                if lab_map[i + x][j + y] == 0:
                    lab_map[i + x][j + y] = 2
                    stack.append((i + x, j + y))
    
    return lab_map

def cnt_room(lab_map):
    cnt = 0
    for li in lab_map:
        cnt += len([x for x in li if x == 0])
    
    return cnt

N,M = map(int, input().strip().split())

lab_map = []
empty = []
virus = []
for i in range(N):
    li = list(map(int, input().strip().split()))
    lab_map.append(li)
    empty += [(i, j) for j, el in enumerate(li) if el == 0]
    virus += [(i, j) for j, el in enumerate(li) if el == 2]


max_size = 0
for item in itertools.combinations(empty, 3):
    cur_map = copy.deepcopy(lab_map)
    
    for i, j in item:
        cur_map[i][j] = 1
    
    spread_virus(cur_map, virus)
    max_size = max(max_size, cnt_room(cur_map))

print(max_size)









