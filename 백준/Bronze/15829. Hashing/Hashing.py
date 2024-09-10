import sys

def to_num(c):
    return "abcdefghijklmnopqrstuvwxyz".find(c) + 1


input = sys.stdin.readline
r = 31
m = 1234567891
l = int(input())

print(sum([x * pow(r, i) for i, x in enumerate(map(to_num, input()))]))
