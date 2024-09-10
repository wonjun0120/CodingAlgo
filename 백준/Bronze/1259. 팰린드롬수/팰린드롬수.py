import sys
input = sys.stdin.readline

while True:
    tc = input().strip()
    if int(tc) == 0: break

    flag = True
    for i in range(len(tc) // 2):
        if tc[i] != tc[len(tc) - 1 - i]:
            print("no")
            flag = False
            break
    if flag:
        print("yes")