# https://school.programmers.co.kr/learn/courses/30/lessons/12987

from collections import defaultdict
from bisect import bisect_left

def solution(A, B):
    answer = 0

    A.sort()
    B.sort()

    data = defaultdict(int)
    for a in A:
        data[a] += 1

    for b in B:
        max_win = bisect_left(A, b) - 1

        while max_win >= 0:
            if data[A[max_win]] > 0:
                data[A[max_win]] -= 1
                answer += 1
                break
            max_win -= 1

    return answer

print(solution([5,1,3,7], [2,2,6,8]))
print(solution([3,4,5,6], [5,1,2,3]))
print(solution([2,2,2,2], [1,1,1,1]))