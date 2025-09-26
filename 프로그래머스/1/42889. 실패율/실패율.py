def solution(N, stages):
    answer = []
    status = {}
    
    for s in stages:
        if s in status.keys():
            status[s] += 1
        else:
            status[s] = 1
    print(status)
    
    fail = []
    p = len(stages)
    for i in range(1, N + 1):
        if i not in status.keys():
            fail.append((i,0))
        else:
            s = status[i]
            print(s, p)
            fail.append((i, (s / p)))
            p -= s
    answer = [x[0] for x in sorted(fail, key= lambda x:x[1], reverse = True)]
    
    return answer