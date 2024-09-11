import sys

input = sys.stdin.readline
n = int(input())

nums = []
for _ in range(n):
    nums.append(int(input()))

answer = 0
max_num = nums[-1]
for i in range(1, n):
    cur_n = nums[n - 1 - i]
    if max_num <= cur_n:
        diff = cur_n - max_num + 1
        answer += diff
        max_num = cur_n - diff
    else:
        max_num = cur_n

print(answer)