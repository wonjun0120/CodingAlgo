import sys
input = sys.stdin.readline

n, m = map(int, input().split())
heights = list(map(int, input().split()))

left, right = 0, max(heights)
answer = 0

while left <= right:
    mid = (left + right) // 2
    total = sum(h - mid for h in heights if h > mid)  # 리스트 컴프리헨션 활용

    if total >= m:  # 원하는 나무 양을 충족하면 높이를 더 높여도 됨
        answer = mid  # 최적값 저장
        left = mid + 1
    else:
        right = mid - 1

print(answer)
