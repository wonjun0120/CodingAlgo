import sys

input = sys.stdin.readline
n = int(input())

words = []

for _ in range(n):
    w = input().strip()
    words.append(w)
    
words = list(set(words))
words.sort()
words.sort(key = lambda x : len(x))
[print(w) for w in words]