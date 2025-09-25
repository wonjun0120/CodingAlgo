def solution(numbers, hand):
    # 각 키의 좌표(행, 열)
    pos = {
        1:(0,0), 2:(0,1), 3:(0,2),
        4:(1,0), 5:(1,1), 6:(1,2),
        7:(2,0), 8:(2,1), 9:(2,2),
        '*':(3,0), 0:(3,1), '#':(3,2)
    }

    left_key, right_key = '*', '#'
    hand = hand.lower()
    answer = []

    for n in numbers:
        if n in (1, 4, 7):
            left_key = n
            answer.append('L')
        elif n in (3, 6, 9):
            right_key = n
            answer.append('R')
        else:
            lx, ly = pos[left_key]
            rx, ry = pos[right_key]
            x, y = pos[n]
            dl = abs(lx - x) + abs(ly - y)
            dr = abs(rx - x) + abs(ry - y)

            if dl < dr:
                left_key = n
                answer.append('L')
            elif dr < dl:
                right_key = n
                answer.append('R')
            else:
                if hand == 'right':
                    right_key = n
                    answer.append('R')
                else:
                    left_key = n
                    answer.append('L')

    return ''.join(answer)
