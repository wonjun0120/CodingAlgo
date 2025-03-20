import itertools

def solution(k, dungeons):
    li = itertools.permutations(dungeons)
    
    answer = 0
    for el in li:
        
        tired = k
        visited = 0
        for dungeon in el:
            if tired >= dungeon[0]:
                tired -= dungeon[1]
                visited += 1
        
        answer = max(answer, visited)
    return answer