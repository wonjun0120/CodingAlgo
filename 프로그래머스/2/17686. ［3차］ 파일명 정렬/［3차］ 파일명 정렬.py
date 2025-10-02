def split_name(s):
    l, r = -1, -1
    
    for i, c in enumerate(s):
        if c.isdigit():
            if l == -1: 
                l = i
        elif l != -1:
            r = i
            break
            
    if r == -1:
        return [s[:l].lower(), int(s[l:])]
    return [s[:l].lower(), int(s[l:r]), s[r:]]
    
def solution(files):
    f = sorted([(split_name(file), file) for file in files], key=lambda x : (x[0][0], x[0][1]))
    return [el[1] for el in f]
    
        