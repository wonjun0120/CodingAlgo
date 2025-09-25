def solution(new_id: str) -> str:
    # 1단계: 소문자
    s = new_id.lower()

    # 2단계: 허용 문자만 남기기
    allowed = set("abcdefghijklmnopqrstuvwxyz0123456789-_.")
    s = ''.join(c for c in s if c in allowed)

    # 3단계: 마침표 연속 치환
    while '..' in s:
        s = s.replace('..', '.')

    # 4단계: 앞뒤 마침표 제거 (빈 문자열 안전)
    s = s.strip('.')

    # 5단계: 빈 문자열이면 'a'
    if not s:
        s = 'a'

    # 6단계: 16자 이상이면 15자로 자르고, 끝이 마침표면 제거
    if len(s) >= 16:
        s = s[:15].rstrip('.')

    # 7단계: 길이 2 이하면 마지막 문자를 반복해 길이 3 만들기
    while len(s) < 3:
        s += s[-1]

    return s
