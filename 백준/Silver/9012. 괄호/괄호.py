import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    stack = []
    ps = input().strip()

    flag = True
    for c in ps:
        if c == '(':
            stack.append("(")
        elif c == ")":
            if len(stack) < 1:
                print("NO")
                flag = False
                break
            stack.pop()
    if flag:
        if len(stack) == 0: print("YES")
        else: print("NO")