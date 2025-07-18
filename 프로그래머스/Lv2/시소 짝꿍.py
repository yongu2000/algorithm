# https://school.programmers.co.kr/learn/courses/30/lessons/152996
from collections import defaultdict

def solution(weights):
    answer = 0
    dic = defaultdict(int)
    weights.sort()
    for weight in weights:
        if dic[weight]:
            answer += dic[weight]
            
        dic[weight] += 1
        dic[weight * 2] += 1
        if weight % 2 == 0:
            dic[(weight//2) * 3] += 1
        if weight % 3 == 0:
            dic[(weight//3) * 4] += 1
    return answer

print(solution([100,100])) # 	4

print(solution([100,180,360,100,270])) # 	4
