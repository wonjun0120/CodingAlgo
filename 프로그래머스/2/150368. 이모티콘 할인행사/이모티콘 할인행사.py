def solution(users, emoticons):
    discounts = (10, 20, 30, 40)
    n = len(emoticons)

    pre = [[emoticons[i] * (100 - d) // 100 for d in discounts] for i in range(n)]

    best_subs = 0
    best_rev = 0
    choice = [0] * n

    def evaluate():
        subs = 0
        rev = 0
        for min_rate, limit in users:
            total = 0
            for i in range(n):
                d = discounts[choice[i]]
                if d >= min_rate:
                    total += pre[i][choice[i]]
            if total >= limit:
                subs += 1
            else:
                rev += total
        return subs, rev

    def dfs(idx):
        nonlocal best_subs, best_rev
        if idx == n:
            subs, r = evaluate()
            if subs > best_subs or (subs == best_subs and r > best_rev):
                best_subs, best_rev = subs, r
            return
        for k in range(4):
            choice[idx] = k
            dfs(idx + 1)

    dfs(0)
    return [best_subs, best_rev]
