import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

pass_dict = {}
for _ in range(n):
    site, pwd = input().strip().split()
    pass_dict[site] = pwd

for _ in range(m):
    site = input().strip()
    print(pass_dict[site])