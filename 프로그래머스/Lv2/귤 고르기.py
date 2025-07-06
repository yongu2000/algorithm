# https://school.programmers.co.kr/learn/courses/30/lessons/138476
from collections import defaultdict

def solution(k, tangerine):
    answer = 0
    counts = defaultdict(int)
    for t in tangerine:
        counts[t] += 1
    tangerine = sorted(list(set(tangerine)), key=lambda x : counts[x], reverse=True)

    for t in tangerine:
        k -= counts[t]
        answer += 1
        if k <= 0:
            return answer

print(solution(6, 	[1, 3, 2, 5, 4, 5, 2, 3])) # 3
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3])) # 2
print(solution(2, 	[1, 1, 1, 1, 2, 2, 2, 3])) # 1




