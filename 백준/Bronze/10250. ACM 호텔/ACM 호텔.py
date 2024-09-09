import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    H, W, N = [int(x) for x in input().split(' ')]
    floor = N % H
    room_num = N // H + 1

    if (floor == 0): 
        floor = H
        room_num -= 1

    floor = str(floor)
    room_num = str(room_num).zfill(2)
    
    print(floor + room_num)