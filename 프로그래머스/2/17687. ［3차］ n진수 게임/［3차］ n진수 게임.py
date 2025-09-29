def change(n, num):
    if num == 0:
        return "0"
    digits = "0123456789ABCDEF"
    res = []
    while num > 0:
        res.append(digits[num % n])
        num //= n
    return ''.join(reversed(res))


def solution(n, t, m, p):
    st = ''
    num = 0
    while len(st) < t * m:
        st += change(n, num)
        num += 1
    return ''.join(st[i] for i in range(p - 1, t * m, m))
