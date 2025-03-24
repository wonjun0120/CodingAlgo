import sys

input = sys.stdin.readline

n = int(input())
tangs = list(map(int, input().split()))

answer = 0
l, r = 0, 0
num_dict = {}
while r < n:
    cur = tangs[r]
    num_dict[cur] = num_dict.get(cur, 0) + 1

    while len(num_dict.keys()) > 2:
        rm = tangs[l]
        num_dict[rm] -= 1

        if num_dict[rm] == 0:
            num_dict.pop(rm)
        l += 1

    answer = max(answer, r - l + 1)
    r += 1

print(answer)

