def solution(survey, choices):
    
    scores = [-1, 3, 2, 1, 0, 1, 2, 3]
    types = list("RTCFJMAN")
    res = {k: 0 for k in types}
    
    
    for s, c in zip(survey, choices):
        a, b = s[0], s[1]
        
        if c == 4:
            pass
        elif c < 4:
            res[a] += scores[c]
        else:
            res[b] += scores[c]
            
    print(res)
    answer = ''
    
    if res['R'] >= res['T']:
        answer += 'R'
    else:
        answer += 'T'
    if res['C'] >= res['F']:
        answer += 'C'
    else:
        answer += 'F'
    if res['J'] >= res['M']:
        answer += 'J'
    else:
        answer += 'M'
    if res['A'] >= res['N']:
        answer += 'A'
    else:
        answer += 'N'
    
    return answer