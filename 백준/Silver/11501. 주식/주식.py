import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    prices = [int(x) for x in input().split(' ')]

    max_price = 0
    answer = 0
    for i in range(len(prices)-1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            answer += (max_price - prices[i])

    print(answer)