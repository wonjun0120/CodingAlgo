import sys
input = sys.stdin.readline

N = int(input())
statement = input().strip()

value = [0.0] * 26
for i in range(N):
    value[i] = float(input().strip())

stack = []

for ch in statement:
    if 'A' <= ch <= 'Z':
        stack.append(value[ord(ch) - ord('A')])
    else:
        b = stack.pop()
        a = stack.pop()

        if ch == '+': stack.append(a + b)
        elif ch == '-': stack.append(a - b)
        elif ch == '*':stack.append(a * b)
        elif ch == '/': stack.append(a / b)

result = stack.pop()
print(f"{result:.2f}")