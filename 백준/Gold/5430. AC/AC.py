import sys
import json
import collections

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    p = input().strip()
    n = int(input())
    li = collections.deque(json.loads(input()))

    is_reversed = False

    for c in p:
        if c == 'R':
            is_reversed = not is_reversed

        if c == 'D':
            if len(li) < 1:
                li = 'error'
                break
            
            if is_reversed:
                li.pop()
            
            if not is_reversed:
                li.popleft()
    
    if li == 'error':
        print(li)
    else:
        if is_reversed:
            li.reverse()
        result = '[' + ','.join(str(num) for num in li) + ']'
        print(result)



