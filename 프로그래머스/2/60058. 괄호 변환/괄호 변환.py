def is_balanced(p):
    start = 0
    for c in p:
        if c == '(':
            start += 1
        if c == ')':
            if start == 0:
                return False
            start -= 1
    return True

def make_reverse(p):
    tmp = ''
    for c in p:
        if c == '(':
            tmp += ')'
        if c == ')':
            tmp += '('
    return tmp

def make_balance(p):
    if p == '': return ''

    idx, right, left = 0, 0, 0
    while idx < len(p):
        if right != 0 and right == left: 
            print(right, left)
            break
        if p[idx] == '(': right += 1
        if p[idx] == ")": left += 1
        idx += 1
        
    u = p[:idx]
    v = p[idx:]
    
    if is_balanced(u):
        return u + make_balance(v)
    else:
        return'(' + make_balance(v) + ')' + make_reverse(u[1:-1])
        
        

def solution(p):
    if is_balanced(p):
        return p
    
    return make_balance(p)
            
    
    