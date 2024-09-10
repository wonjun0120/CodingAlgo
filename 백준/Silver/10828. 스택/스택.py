import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    cmd = input().strip().split(' ')
    
    if cmd[0] == "push":
        stack.append(cmd[1])

    elif cmd[0] == "pop":
        if len(stack) < 1:
            print(-1)
        else:
            print(stack.pop())

    elif cmd[0] == "size":
        print(len(stack))

    elif cmd[0] == "empty":
        print(1 if len(stack) == 0 else 0)

    elif cmd[0] == "top":
        if len(stack) < 1:
            print(-1)
        else:
            print(stack[-1])