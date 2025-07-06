# https://school.programmers.co.kr/learn/courses/30/lessons/131701

def solution(elements):
    cycle = elements + elements
    nums = set()
    for i in range(len(elements)):
        for length in range(1, len(elements)):
            nums.add(sum(cycle[i:i+length]))
    return len(nums)+1

print(solution([7,9,1,1,4])) # 3




