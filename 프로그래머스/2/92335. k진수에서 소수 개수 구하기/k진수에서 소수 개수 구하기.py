import math

def to_base(n, base):
    if n == 0: return 0
    
    digits = "0123456789ABCDE"
    
    buf = []
    while n > 0:
        n, r = divmod(n, base)
        buf.append(digits[r])
    return "".join(reversed(buf))

def is_prime(n):
    if n == '': return 0
    n = int(n)
    if n == 1: return 0
    elif n == 2: return 1
    elif n % 2 == 0: return 0
    
    limit = math.isqrt(n)
    i = 3
    while i <= limit:
        if n % i == 0:
            return 0
        i += 2
    return 1
    

def solution(n, k):
    kbase = to_base(n, k)
    print(kbase)
    
    li = kbase.split('0')
    return sum([is_prime(el) for el in li])
        