import sys

input = sys.stdin.readline

n = int(input())

nums = []
n_dict = {}
for _ in range(n):
    num = int(input())
    nums.append(num)
    if num in n_dict.keys():
        n_dict[num] += 1
        continue
    n_dict[num] = 1

nums.sort()
print(round(sum(nums) / len(nums)))
print(nums[n // 2])

freq = max(n_dict.values())
numbers = []
for key, value in n_dict.items():
    if value == freq:
        numbers.append(key)

if len(numbers) == 1:
    print(numbers[0])
else:
    print(sorted(numbers)[1])

print(nums[-1] - nums[0])