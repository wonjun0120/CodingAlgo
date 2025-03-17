import sys

input = sys.stdin.readline

n, m, b = map(int, input().split())

field = []
field_dict = {}
for _ in range(n):
    input_li = list(map(int, input().split()))
    field.append(input_li)

    for i in input_li:
        if i in field_dict:
            field_dict[i] += 1
        else:
            field_dict[i] = 1


min_time = float('inf')
inventory = b
tmp = 0
for height in range(257):
    rm_block, add_block = 0, 0

    for block, cnt in field_dict.items():
        if block < height:
            add_block += (height - block) * cnt
        else:
            rm_block += (block - height) * cnt
    
    if rm_block + b - add_block < 0:
        continue

    time = rm_block * 2 + add_block
    if time <= min_time:
        min_time = time
        tmp = height

print(min_time, tmp)
