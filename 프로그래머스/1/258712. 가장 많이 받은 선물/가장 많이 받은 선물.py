def solution(friends, gifts):
    n = len(friends)
    name_to_idx = {name: i for i, name in enumerate(friends)}

    # 보낸/받은 횟수와 페어별 교환 테이블
    sent = [0] * n
    received = [0] * n
    table = [[0] * n for _ in range(n)]

    for gift in gifts:
        give, take = gift.split()
        gi = name_to_idx[give]
        ti = name_to_idx[take]
        sent[gi] += 1
        received[ti] += 1
        table[gi][ti] += 1

    gift_index = [sent[i] - received[i] for i in range(n)]
    answer = [0] * n

    for i in range(n):
        for j in range(i + 1, n):
            a, b = table[i][j], table[j][i]
            if a > b:
                answer[i] += 1
            elif a < b:
                answer[j] += 1
            else:
                if gift_index[i] > gift_index[j]:
                    answer[i] += 1
                elif gift_index[i] < gift_index[j]:
                    answer[j] += 1

    return max(answer) if answer else 0
