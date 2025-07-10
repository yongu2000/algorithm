# https://school.programmers.co.kr/learn/courses/30/lessons/17680
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
            elif cacheSize > 0:
                cache.popleft()
                cache.append(city)

    return answer


print(solution(2, 	["Jeju", "Pangyo", "NewYork", "newyork"])) # 16
print(solution(0, 	["Jeju", "Pangyo", "Seoul", "NewYork", "LA"])) # 25




