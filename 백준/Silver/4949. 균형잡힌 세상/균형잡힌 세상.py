import sys

input = sys.stdin.readline

while True:
    n = input()
    # print(n)
    if n.rstrip() == '.':
        break

    stack = []
    flag = True
    for c in n:
        if c == '(':
            stack.append('(')
        elif c == '[':
            stack.append('[')
        elif c == ')':
            if len(stack) < 1 or stack[-1] != '(':
                print("no")
                flag = False
                break
            stack.pop()
        elif c == ']':
            if len(stack) < 1 or stack[-1] != '[':
                print("no")
                flag = False
                break
            stack.pop()
    if flag:
        if len(stack) < 1:
            print("yes")
        else:
            print("no")
