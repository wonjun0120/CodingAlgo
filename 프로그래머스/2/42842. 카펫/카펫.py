def solution(brown, yellow):
    answer = []
    if yellow == 1:
        return [3, 3]
        
    
    for i in range(1, yellow // 2 + 1):
        if yellow % i == 0:
            yx, yy = i, yellow/i
            need_brown = (yx + 2 + yy) * 2
            
            if need_brown == brown:
                return [yy + 2, yx + 2]
    return answer