import sys
input = sys.stdin.readline

a, b = [int(x) for x in input().split(' ')]

def gcd (a, b):
    while(b != 0):
        r = a % b
        a = b
        b = r
    return a

def lcm (a, b):
    return a * b // gcd(a, b)

print(gcd(a, b))
print(lcm(a, b))