import sys

input = sys.stdin.readline

n = int(input())
li = list(map(int, input().split()))

sorted_li = sorted(set(li))
li_dict = {e : i for i, e in enumerate(sorted_li)}

print(' '.join([str(li_dict.get(i)) for i in li]))

