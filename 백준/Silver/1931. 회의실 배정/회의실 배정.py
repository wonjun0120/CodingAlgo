import sys
input = sys.stdin.readline

n = int(input())

rooms = []
for i in range(n):
    rooms.append(list(map(int, input().split())))

rooms.sort(key = lambda x: (x[1], x[0]))

before_end = 0
answer = 0
for start, end in rooms:
    if before_end <= start:
        answer += 1
        before_end = end


print(answer)

