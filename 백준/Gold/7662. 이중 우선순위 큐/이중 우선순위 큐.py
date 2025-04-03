import sys
import heapq
from collections import defaultdict

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    k = int(input())
    min_heap = []
    max_heap = []
    counter = defaultdict(int)

    for _ in range(k):
        c, n = input().split()
        n = int(n)

        if c == 'I':
            heapq.heappush(min_heap, n)
            heapq.heappush(max_heap, -n)
            counter[n] += 1

        elif c == 'D':
            if n == 1:
                while max_heap:
                    num = -heapq.heappop(max_heap)
                    if counter[num] > 0:
                        counter[num] -= 1
                        break
            else:
                while min_heap:
                    num = heapq.heappop(min_heap)
                    if counter[num] > 0:
                        counter[num] -= 1
                        break

    max_val, min_val = None, None

    while max_heap:
        num = -heapq.heappop(max_heap)
        if counter[num] > 0:
            max_val = num
            break

    while min_heap:
        num = heapq.heappop(min_heap)
        if counter[num] > 0:
            min_val = num
            break

    if max_val is None or min_val is None:
        print("EMPTY")
    else:
        print(f"{max_val} {min_val}")
