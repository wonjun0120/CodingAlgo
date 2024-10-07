import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

pocketmon_dict = {}
pocketmon2num = {}

for i in range(n):
    pocketmon = input().strip()
    num = i + 1

    pocketmon_dict[num] = pocketmon
    pocketmon2num[pocketmon] = num


for _ in range(m):
    exp = input().strip()
    if exp.isdigit():
        print(pocketmon_dict[int(exp)])
    if not exp.isdigit():
        print(pocketmon2num[exp])