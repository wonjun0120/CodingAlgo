from collections import deque

def solution(queue1, queue2):
    dq1 = deque(queue1)
    dq2 = deque(queue2)

    s1 = sum(dq1)
    s2 = sum(dq2)
    total = s1 + s2

    if total % 2 == 1:
        return -1
    target = total // 2
    max_val = 0
    if dq1:
        max_val = max(max_val, max(dq1))
    if dq2:
        max_val = max(max_val, max(dq2))
    if max_val > target:
        return -1

    if s1 == target:
        return 0

    moves = 0
    limit = 3 * (len(queue1) + len(queue2))

    while moves <= limit and s1 != target:
        if s1 > target:
            if not dq1:
                return -1
            x = dq1.popleft()
            dq2.append(x)
            s1 -= x
        else:  
            if not dq2:  
                return -1
            y = dq2.popleft()
            dq1.append(y)
            s1 += y
        moves += 1

    return moves if s1 == target else -1
