# https://school.programmers.co.kr/learn/courses/30/lessons/12927

import heapq

def solution(n, works):
    heap = []
    for work in works:
        heapq.heappush(heap, -work)
        
    while n > 0 and heap:
        max_work = -heapq.heappop(heap)
        if max_work >= 1:
            heapq.heappush(heap, -(max_work - 1))
        n -= 1
        
    answer = 0
    for num in heap:
        answer += num**2
    return answer

print(solution(4, [4, 3, 3]))