import collections
def time2int(s):
    hh, mm = s.split(':')
    return int(hh) * 60 + int(mm)
    

def split_rythm(rythm):
    mli = collections.deque([])
    for i, c in enumerate(list(rythm)):
        if i == 0: mli.append(c)
        else:
            if c == '#':
                tmp = mli.pop()
                mli.append(tmp + '#')
            else:
                mli.append(c)
    return list(mli)
    
def is_include(m, r):
    n, k = len(r), len(m)
    if k > n:
        return False
    for i in range(n - k + 1):
        if r[i:i + k] == m:
            return True
    return False
                
def solution(m, musicinfos):
    answer = (0, '(None)')
    for music in musicinfos:
        start, end, title, rythm = music.split(',')
        run_time = time2int(end) - time2int(start)
        
        m, rythm = split_rythm(m), split_rythm(rythm)
        
        while len(rythm) < run_time:
            rythm *= 2
        
        rythm = rythm[:run_time]
        
        if is_include(m, rythm): 
            if answer[0] < run_time:
                answer = (run_time, title)
    return answer[1]