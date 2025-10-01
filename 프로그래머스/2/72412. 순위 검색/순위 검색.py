from collections import defaultdict

def lower_bound(a, x):
    lo, hi = 0, len(a)
    while lo < hi:
        mid = (lo + hi) // 2
        if a[mid] < x:
            lo = mid + 1
        else:
            hi = mid
    return lo

def solution(info, query):
    db = defaultdict(list)

    for s in info:
        a, b, c, d, sc = s.split()
        sc = int(sc)
        attrs = [a, b, c, d]
        for mask in range(16):
            key = []
            for i in range(4):
                key.append('-' if (mask & (1 << i)) else attrs[i])
            db[' '.join(key)].append(sc)

    for k in db:
        db[k].sort()

    answer = []
    for q in query:
        q = q.replace(' and ', ' ')
        a, b, c, d, thr = q.split()
        key = f'{a} {b} {c} {d}'
        thr = int(thr)
        lst = db.get(key, [])
        idx = lower_bound(lst, thr)
        answer.append(len(lst) - idx)

    return answer
