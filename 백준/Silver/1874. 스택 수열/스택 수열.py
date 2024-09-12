import sys

input = sys.stdin.readline
n = int(input())

stack = []
answer = []

cur = 1
for i in range(n):
    num = int(input())
    while cur <= num:       
        stack.append(cur)
        answer.append("+")
        cur += 1
 
    if stack[-1] == num:    
        stack.pop()        
        answer.append("-")
        
    else:                   
        print("NO")         
        sys.exit(0)               

[print(x) for x in answer]