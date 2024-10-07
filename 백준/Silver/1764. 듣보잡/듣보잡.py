import sys

input = sys.stdin.readline

n, m = [int(x) for x in input().split()]

dut = {}
bo = []

for _ in range(n):
    person = input().strip()
    dut[person] = True

for _ in range(m):
    person = input().strip()
    if person in dut.keys():
        bo.append(person)

print(len(bo))
bo.sort()
for el in bo:
    print(el)
