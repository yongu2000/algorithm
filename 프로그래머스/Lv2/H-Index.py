# https://school.programmers.co.kr/learn/courses/30/lessons/42747


from bisect import bisect_left

def solution1(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    for i in range(10_001):
        h = n - bisect_left(citations, i)
        if h >= i:
            answer = i
    return answer


def solution2(citations):
    answer = 0
    citations.sort()
    n = len(citations)
    left = 0
    right = n
    
    while left <= right:
        mid = (left+right) // 2
        h = n - bisect_left(citations, mid)
        
        if h >= mid:
            left = mid + 1
            answer = mid
        else:
            right = mid - 1

    return answer

print(solution2([3, 0, 6, 1, 5]))
print(solution2([0]))
print(solution2([3, 3, 3, 4]))
print(solution2([1]))

