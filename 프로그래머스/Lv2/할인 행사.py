# https://school.programmers.co.kr/learn/courses/30/lessons/131127
from collections import defaultdict

def solution(want, number, discount):
    answer = 0
    n = sum(number)
    data = defaultdict(int)
    left = 0
    right = n-1

    for i in range(n):
        data[discount[i]] += 1

    while right < len(discount):
        ok = True
        for i in range(len(want)):
            if data[want[i]] < number[i]:
                ok = False
                break
        if ok:
            answer += 1

        data[discount[left]] -= 1
        left += 1
        right += 1
        if right == len(discount):
            break
        data[discount[right]] += 1


    return answer


print(solution(["banana", "apple", "rice", "pork", "pot"],
               [3, 2, 2, 2, 1],
               ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
               )) # 3
print(solution(["apple"],
               [10],
               	["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana"]
               )) # 3




