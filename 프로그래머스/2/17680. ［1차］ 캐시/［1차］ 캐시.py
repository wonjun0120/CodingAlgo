from collections import deque

def solution(cacheSize, cities):
    cache = deque([])
    
    answer = 0
    
    for city in cities:
        city = city.lower()
        
        is_in = False
        idx = -1
        for i, c in enumerate(cache):
            if c == city:
                is_in = True
                idx = i
                break
        
        if is_in:
            answer += 1
            cache.remove(city)
            cache.append(city)
        
        else:
            answer += 5
            cache.append(city)
        
        if len(cache) > cacheSize:
            cache.popleft()


    return answer
    