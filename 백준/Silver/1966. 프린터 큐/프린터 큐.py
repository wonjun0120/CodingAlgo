import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = [int(x) for x in input().strip().split()]
    priorities = [(i, int(x)) for i, x in enumerate(input().strip().split())]
    
    cnt = 1
    while len(priorities) > 0:
        target = priorities[0]
        flag = False
        if len(priorities) == 1:
            print(cnt)
            break

        for i in range(1, len(priorities)):
            if priorities[i][1] > target[1]:
                priorities.append(target)
                priorities.pop(0)
                break
            if i == len(priorities) - 1:
                if target[0] == m:
                    print(cnt)
                    flag = True
                cnt += 1
                priorities.pop(0)
        if flag:
            break

