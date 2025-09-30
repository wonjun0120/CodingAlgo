def split_number(s: str):
    l = None
    for i, c in enumerate(s):
        if c.isdigit():
            l = i
            break

    if l is None:
        return s, "", ""

    r = l
    n = len(s)
    while r < n and s[r].isdigit():
        r += 1

    left = s[:l]
    mid  = s[l:r]
    right = s[r:]
    return (left.lower(), int(mid), s)


def solution(files):
    return [x[-1] for x in sorted([split_number(n) for n in files], key=lambda x: (x[0], x[1]))]