def solution(relation):
    n = len(relation[0])
    answer = []
    path = []

    def is_unique(cols):
        seen = set()
        for row in relation:
            seen.add(tuple(row[c] for c in cols))
        return len(seen) == len(relation)

    def violates_minimal_with_answer(cols):
        s = set(cols)
        for key in answer:
            if set(key).issubset(s):
                return True
        return False

    def has_unique_proper_subset(cols):
        k = len(cols)
        if k <= 1:
            return False
        idxs = list(cols)
        limit = (1 << k) - 1
        for mask in range(1, limit):
            sub = [idxs[j] for j in range(k) if (mask >> j) & 1]
            if is_unique(sub):
                return True
        return False

    def back(start):
        for i in range(start, n):
            path.append(i)

            if violates_minimal_with_answer(path):
                path.pop()
                continue

            if is_unique(path):
                if not has_unique_proper_subset(path):
                    answer.append(tuple(path))
                path.pop()
                continue
            back(i + 1)
            path.pop()

    back(0)
    return len(answer)
