def solution(diffs, times, limit):
    max_diffs = max(diffs)
    
    left = 1
    right = max_diffs
    passed = []
    while left < right:
        acc_time = 0
        flag = False
        level = (left + right) // 2
        
        for i in range(len(diffs)):
            diff = diffs[i]
            time = times[i]
            
            if diff <= level:
                acc_time += time
            elif diff > level:
                time_prev = 0
                if i > 0:
                    time_prev = times[i - 1]
                acc_time += ((time + time_prev) * (diff - level) + time)
                
        if limit < acc_time:
            left = level + 1
        if limit >= acc_time:
            passed.append(level)
            right = level
    
    return left