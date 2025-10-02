def solution(s):
    s = s[2:-2]
    
    li = sorted(s.split('},{'), key=lambda x:len(x))
    
    answer = []
    for el in li:
        el = el.split(',')
        for n in el:
            n = int(n)
            if n in answer: continue
            answer.append(n)
            
    return list(answer)
    