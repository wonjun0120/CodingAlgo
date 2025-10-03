from collections import deque

def solution(queue1, queue2):
    q1, q2 = deque(queue1), deque(queue2)
    s1, s2 = sum(q1), sum(q2)
    total = s1 + s2
    if total % 2 != 0:
        return -1
    target = total // 2

    if max(queue1 + queue2) > target:
        return -1

    if s1 == target:
        return 0

    limit = 2 * (len(q1) + len(q2) + 1)
    cnt = 0

    while cnt <= limit and s1 != target:
        if s1 > target:
            if not q1:
                return -1
            x = q1.popleft()
            q2.append(x)
            s1 -= x
        else:
            if not q2:
                return -1
            x = q2.popleft()
            q1.append(x)
            s1 += x
        cnt += 1

    return cnt if s1 == target else -1
