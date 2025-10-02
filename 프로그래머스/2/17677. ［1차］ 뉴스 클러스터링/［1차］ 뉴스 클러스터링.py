def split_str(s):
    li = []
    
    for i in range(1, len(s)):
        tmp = s[i - 1: i + 1].lower()
        if tmp[0] not in list('abcdefghijklmnopqrstuvwxyz'):
            continue
        if tmp[1] not in list('abcdefghijklmnopqrstuvwxyz'):
            continue
        li.append(tmp)
    return li

def _count_elems(li):
    d = {}
    for x in li:
        d[x] = d.get(x, 0) + 1
    return d

def diff(s1, s2):
    c1, c2 = _count_elems(s1), _count_elems(s2)
    res = []
    for k in c1:
        m = min(c1[k], c2.get(k, 0))
        if m > 0:
            res.extend([k] * m)
    return res

def sums(s1, s2):
    c1, c2 = _count_elems(s1), _count_elems(s2)
    res = []
    keys = set(c1) | set(c2)
    for k in keys:
        m = max(c1.get(k, 0), c2.get(k, 0))
        if m > 0:
            res.extend([k] * m)
    return res

def jacad(s1, s2):
    a = sums(s1, s2)
    b = diff(s1, s2)
    
    print(a)
    print(b)
    
    if len(a) == 0: return 1
    if len(b) == 0: return 0
    return len(b) / len(a)

def solution(str1, str2):
    str1, str2 = split_str(str1), split_str(str2)
    
    return int(jacad(str1, str2) * 65536)