import sys

input = sys.stdin.readline

n = int(input())
n_li = [int(x) for x in input().strip().split()]
n_dict = {}
for el in n_li:
    if el in n_dict.keys():
        n_dict[el] += 1
        continue
    
    n_dict[el] = 1
    

m = int(input())
m_li = [int(x) for x in input().strip().split()]
answer = []
for el in m_li:
    if el in n_dict.keys():
        answer.append(str(n_dict[el]))
        continue
    answer.append(str(0))


print(' '.join(answer))