def solution(msg):
    word_dict = {}
    for i, word in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1):
        word_dict[word] = i
        
    # print(word_dict)
    
    l, r = 0, 1
    answer = []
    lst = 27
    before = -1
    while l < r and r <= len(msg):
        cur = msg[l:r]
        if word_dict.get(cur):
            before = word_dict[cur]
            r += 1
        else:
            word_dict[cur] = lst
            answer.append(before)
            l = r - 1
            lst += 1
    answer.append(before)
    return answer