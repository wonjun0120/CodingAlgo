import sys
input = sys.stdin.readline

n = int(input())
    
factorial = 1
for num in range(1, n + 1):
    factorial *= num

factorial = str(factorial)

if len(factorial) < 2: 
    print(0)

else:
    answer = 0
    for i in range(len(factorial) - 1, -1, -1):
        if factorial[i] == '0':
            answer += 1
        else: 
            break

    print(answer)