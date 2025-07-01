import sys
from itertools import combinations

input = sys.stdin.readline
N,L,R,X = map(int, input().strip().split())
difficulty_levels = list(map(int, input().strip().split()))

cnt = 0

for case_cnt in range(2, len(difficulty_levels) + 1):
    for cases in combinations(difficulty_levels, case_cnt):
        if L <= sum(cases) <= R and max(cases)-min(cases) >= X:
            cnt+=1
print(cnt)
