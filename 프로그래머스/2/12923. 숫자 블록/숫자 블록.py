def solution(begin, end):
    def get_block(num):
        if num == 1:
            return 0

        max_block = 1  # 기본값은 1번 블록
        limit = int(num ** 0.5) + 1

        for i in range(2, limit):
            if num % i == 0:
                pair = num // i

                if pair <= 10_000_000:
                    return pair 
                if i <= 10_000_000:
                    max_block = max(max_block, i)

        return max_block

    return [get_block(num) for num in range(begin, end + 1)]
