import sys

input = sys.stdin.readline
n, k = [int(x) for x in input().split()]

def recur(n, k):
    if k == 0: return 1
    if n == k: return 1

    return recur(n - 1, k - 1) + recur(n - 1, k)

print(recur(n, k))