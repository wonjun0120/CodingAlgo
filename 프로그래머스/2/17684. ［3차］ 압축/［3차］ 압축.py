def solution(msg):
    book = {k: i for i, k in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", 1)}
    lst = 27
    
    answer = []
    l, r = 0, 1
    while l < r and r <= len(msg):
        cur = msg[l:r]
        if cur == '': continue
        if cur in book:
            r += 1
        else:
            answer.append(book[cur[:-1]])
            book[cur] = lst
            lst += 1
            l = r - 1
    answer.append(book[msg[l:r-1]])
    return answer
            
    