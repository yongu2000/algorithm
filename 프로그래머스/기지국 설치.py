# https://school.programmers.co.kr/learn/courses/30/lessons/12979
import math

def solution(n, stations, w):
    answer = 0
    
    power = w*2 + 1

    position = 1        

    for station in stations:
        left = station - w
        if position < left:
            count = left - position
            answer += math.ceil(count / power)
        position = station + w + 1

    if position < n:
        count = n - position
        answer += math.ceil(count / power)
    
    if position == n:
        answer += 1
        
    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
print(solution(6, [2], 1))

print(solution(13, [3, 7, 11], 1)) #
print(solution(5, [3], 2))
print(solution(6, [3], 2)) #
print(solution(16, [1, 16], 2))
print(solution(6, [4], 2))
print(solution(11, [1, 4], 1))
print(solution(11, [1, 5], 1))
print(solution(5, [1, 2, 3, 4, 5], 1))
print(solution(200000000, [100000000], 5))



