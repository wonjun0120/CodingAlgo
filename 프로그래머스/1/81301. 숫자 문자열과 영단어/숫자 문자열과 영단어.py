def solution(s):
    num_eng = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
    }
    
    answer = ""
    tmp = ""
    for c in s + " ":
        if c.isdigit():
            if tmp != "":
                answer += str(num_eng[tmp])
            answer += c
            tmp = ""
        elif tmp in num_eng.keys():
            answer += str(num_eng[tmp])
            tmp = c
        else:
            tmp += c
    return int(answer)
        