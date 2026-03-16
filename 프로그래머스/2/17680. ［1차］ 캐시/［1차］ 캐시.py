from collections import deque

def solution(cacheSize, cities):
    answer = 0
    
    cache = deque()
    for city in cities:
        city = city.lower()
        if city in cache:
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:
            answer += 5
            if len(cache) < cacheSize:
                cache.append(city)
            else:
                if cache:
                    cache.popleft()
                if len(cache) < cacheSize:
                    cache.append(city)
    
    return answer