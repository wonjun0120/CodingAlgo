from collections import deque
def solution(cacheSize, cities):
    cache = deque([])
    cities = [c.lower() for c in cities]
    
    if cacheSize < 1:
        return len(cities) * 5
    
    answer = 0
    for city in cities:
        if city not in cache:
            answer += 5
            if len(cache) >= cacheSize:
                cache.popleft()
            
            cache.append(city)
            
        else:
            cache.remove(city)
            cache.append(city)
            answer += 1
            
    return answer