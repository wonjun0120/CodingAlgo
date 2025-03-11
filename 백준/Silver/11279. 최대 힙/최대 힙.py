import sys
import heapq

input = sys.stdin.readline

n = int(input())

heap = []
for _ in range(n):
    num = int(input())
    if num == 0:
        print(heapq.heappop(heap)[1] if heap else 0)
    else:
        heapq.heappush(heap, (-1 * num, num))


