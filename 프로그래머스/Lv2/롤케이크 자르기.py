# https://school.programmers.co.kr/learn/courses/30/lessons/132265
from collections import defaultdict
def solution(topping):
    answer = 0
    n = len(topping)

    left_data = defaultdict(int)
    right_data = defaultdict(int)

    left_type = set()
    right_type = set(topping)
    for i in range(n):
        right_data[topping[i]] += 1

    for cut in range(n):
        now = topping[cut]
        left_type.add(now)
        left_data[now] += 1
        right_data[now] -= 1
        if right_data[now] == 0:
            right_type.remove(now)
        
        if len(left_type) == len(right_type):
            answer += 1

    return answer


print(solution([1, 2, 1, 3, 1, 4, 1, 2])) # 2
print(solution([1, 2, 3, 1, 4])) # 0




