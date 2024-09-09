import sys

def is_prime_number(x):
    for i in range(2, x):
        if x % i == 0:
            return 0 
    return 1

input = sys.stdin.readline
n = int(input())
nums = [is_prime_number(int(x)) for x in input().split(' ') if int(x) > 1]
print(sum(nums))