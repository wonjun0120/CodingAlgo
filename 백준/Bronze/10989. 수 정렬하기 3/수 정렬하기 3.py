import sys
input = sys.stdin.readline

n = int(sys.stdin.readline())

num_list = [0] * 10001
for i in range(n):
    num_list[(int(input()))] += 1

for i, num in enumerate(num_list):
    if num > 0:
        for _ in range(num):
            print(i)