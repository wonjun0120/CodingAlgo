def solution(today, terms, privacies):
    def to_days(date_str):
        y, m, d = map(int, date_str.split("."))
        return y * 12 * 28 + (m - 1) * 28 + d

    term_months = {}
    for t in terms:
        k, v = t.split()
        term_months[k] = int(v)

    today_days = to_days(today)

    answer = []
    for idx, p in enumerate(privacies, start=1):
        start_str, term_key = p.split()
        start_days = to_days(start_str)

        expire_days = start_days + term_months[term_key] * 28 - 1

        if today_days > expire_days:
            answer.append(idx)

    return answer
