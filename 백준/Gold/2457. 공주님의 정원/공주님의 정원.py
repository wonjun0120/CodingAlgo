import sys
input = sys.stdin.readline

def date_to_int(month, day):
    return month * 100 + day

n = int(input())

flowers = []
for _ in range(n):
    sm, sd, em, ed = map(int, input().split())
    flowers.append((date_to_int(sm, sd), date_to_int(em, ed)))

start = date_to_int(3, 1)
end = date_to_int(11, 30)

flowers.sort()

current_end = start 
count = 0  
i = 0  
max_end = 0 

while current_end <= end:
    found = False
    while i < n and flowers[i][0] <= current_end:
        max_end = max(max_end, flowers[i][1])
        i += 1
        found = True

    if not found:  
        break

    count += 1
    current_end = max_end  

if current_end <= end: 
    print(0)
else:
    print(count)