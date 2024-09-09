import sys
input = sys.stdin.readline


def calc_sub_exp(exp):
    split_exp = exp.split('+')
    return (sum([int(x) for x in split_exp]))   


input_exp = input()
exp = [calc_sub_exp(x) for x in input_exp.split('-')]

answer = exp[0]
for i in range(len(exp) - 1):
    answer -= exp[i + 1]

print(answer)

