import sys
input = sys.stdin.readline

while True:
    testcase = input()
    
    pows = [pow(int(x), 2) for x in testcase.split(' ')]
    if sum(pows) == 0:
        break

    if pows[0] == pows[1] + pows[2] or \
        pows[1] == pows[0] + pows[2] or \
        pows[2] == pows[0] + pows[1]:
        print("right")
    else: 
        print("wrong")