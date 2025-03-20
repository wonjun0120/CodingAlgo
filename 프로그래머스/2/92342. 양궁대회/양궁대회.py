import itertools

def solution(n, info):
    answer = [-1]
    max_diff = 0
    # break_num = 0
    for el in itertools.combinations_with_replacement(reversed([num for num in range(11)]), n):
        lion_info = []
        for i in range(11):
            if i in el:
                lion_info.append(el.count(i))
            else:
                lion_info.append(0)
        
        lion, appeach = 0, 0
        for i in range(11):
            if lion_info[i] + info[i] == 0:
                continue
                
            if lion_info[i] <= info[i]:
                appeach += (10 - i)
                
            else:
                lion += (10 - i)
                
        # print(lion_info, lion, appeach, lion - appeach)
        if max_diff < (lion - appeach):
            max_diff = (lion- appeach)
            answer = lion_info
        # break_num += 1
        # if break_num == 50:
        #     break
        
    return answer
    
            
        
        
            