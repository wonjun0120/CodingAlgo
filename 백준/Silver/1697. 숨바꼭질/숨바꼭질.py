import sys
import collections

input = sys.stdin.readline

n, k = map(int, input().split())

answer = 0
queue = [n]
is_visit = set()
while queue:
    tmp = []
    for el in queue:
        if el == k:
            print(answer)
            sys.exit(0)

        if el < k:
            if el * 2 not in is_visit:
                tmp.append(el * 2)
                is_visit.add(el * 2)
            if el + 1 not in is_visit:
                tmp.append(el + 1)
                is_visit.add(el + 1)
        if el - 1 not in is_visit:
            tmp.append(el - 1)
            is_visit.add(el - 1)
    answer += 1
    queue = tmp

