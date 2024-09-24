import sys
input = sys.stdin.readline

n = int(input())
n_dict = {}
a_s = [int(x) for x in input().strip().split()]
for el in a_s:
    n_dict[el] = 1

m = int(input())
ms = [int(x) for x in input().strip().split()]

for el in ms:
    if el in n_dict.keys():
        print(n_dict[el])
    else:
        print(0)