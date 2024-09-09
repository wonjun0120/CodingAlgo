import sys
input = sys.stdin.readline

nums = [int(x) for x in input().split(' ')]

print(sum([pow(x, 2) for x in nums]) % 10)