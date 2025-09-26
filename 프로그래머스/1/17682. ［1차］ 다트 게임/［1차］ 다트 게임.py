def solution(dartResult):
    records = []
    tmp = ''
    for i, c in enumerate(dartResult):
        if i == 0:
            tmp = c
        elif c.isdigit() and not tmp.isdigit():
            records.append(tmp)
            tmp = c
        else:
            tmp += c
    records.append(tmp)
    
    answer = 0
    before = 0
    for rec in records:
        is_double = False
        is_minus = False
        if len(rec) >= 3:
            option = rec[-1]
            if option == "*":
                answer += before
                is_double = True
            if option == "#":
                is_minus = True
        j = 0
        while j < len(rec) and rec[j].isdigit():
            j += 1
        score = int(rec[:j])   # '10' 같은 두 자리도 안전
        area  = rec[j]         # 'S' | 'D' | 'T'

        if area == 'D':
            score = score ** 2
        if area == 'T':
            score = score ** 3
        
        print(score)
        
        if is_double:
            score *= 2
        if is_minus:
            score *= -1
        
        answer += score
        before = score
                
    return answer