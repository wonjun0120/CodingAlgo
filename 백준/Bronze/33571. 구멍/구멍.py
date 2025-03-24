# 문자별 구멍 개수 정의
hole_count = {
    'A': 1, 'B': 2, 'D': 1, 'O': 1, 'P': 1, 'Q': 1, 'R': 1,
    'a': 1, 'b': 1, 'd': 1, 'e': 1, 'g': 1, 'o': 1, 'p': 1, 'q': 1,
    '@': 1
}

S = input()  # 입력 받기
total = 0

for ch in S:
    total += hole_count.get(ch, 0)  # 정의되지 않은 문자는 0개로 처리

print(total)
