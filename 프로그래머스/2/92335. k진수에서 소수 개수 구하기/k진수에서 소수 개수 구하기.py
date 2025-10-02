def changebase(base, num):
    numbers = '0123456789ABCDEF'
    
    res = ''
    if num == 0: return '0' 
    while num > 0:
        a, b = divmod(num, base)
        res += str(b)
        num = a
    return ''.join(reversed(list(res)))

def is_prime(num):
    import math
    num = int(num)
    
    if num < 2: return False
    if num == 2 : return True
    for i in range(3, int(math.sqrt(num) + 1)):
        if num % i == 0:
            return False
    return True

def solution(n, k):
    num = changebase(k, n).split('0')
    cnt = 0
    for el in num:
        if el == '':
            continue
        if is_prime(el):
            cnt += 1
    return cnt
    