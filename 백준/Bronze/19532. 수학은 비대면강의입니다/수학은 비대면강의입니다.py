import sys
input = sys.stdin.readline

a, b, c, d, e, f = [int(x) for x in input().strip().split()]

x = ((e * c) - (b * f)) / ((a * e) - (b * d))
y = ((d * c) - (a * f)) / ((d * b) - (a * e))

print(f"{int(x)} {int(y)}")