def changebase(base, num):
    numbers = '0123456789ABCDEF'
    res = ''
    num = int(num)
    if num == 0: return '0'
    while num > 0:
        a, b = divmod(num, base)
        res += numbers[b]
        num = a
    
    return ''.join(reversed(list(res)))

def solution(n, t, m, p):
    s = ''
    i = 0
    while len(s) <= (m * (t + 1)):
        s += changebase(n, i)
        i += 1
    
    # print(s)
    answer = ''
    
    for i in range(p - 1, m * (t - 1) + p, m):
        answer += s[i]
    
    return answer