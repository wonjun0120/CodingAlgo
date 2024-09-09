import sys
input = sys.stdin.readline

n = int(input())
sizes = [int(x) for x in input().split(' ')]
t, p = [int(x) for x in input().split(' ')]

t_sum = 0
for s in sizes:
    if s > 0:
        if s%t == 0:
            t_sum += (s//t)
        else:
            t_sum += (s//t+1)

print(t_sum)
print(n // p, n % p)