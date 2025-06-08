# https://school.programmers.co.kr/learn/courses/30/lessons/42628#

import heapq
from collections import defaultdict

def solution(operations):
    
    max_heap = []
    min_heap = []
    
    count = defaultdict(int)
    
    for operation in operations:
        command, num = operation.split()
        num = int(num)
        
        if command == "I":
            count[num] += 1
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        else:
            if num == 1:
                while max_heap and count[-max_heap[0]] == 0:
                    heapq.heappop(max_heap)
                if max_heap:
                    count[-heapq.heappop(max_heap)] -= 1
            elif num == -1:
                while min_heap and count[min_heap[0]] == 0:
                    heapq.heappop(min_heap)
                if min_heap:
                    count[heapq.heappop(min_heap)] -= 1

    while min_heap and count[min_heap[0]] == 0:
        heapq.heappop(min_heap)
    while max_heap and count[-max_heap[0]] == 0:
        heapq.heappop(max_heap)

    answer = []
    if not min_heap and not max_heap:
        answer = [0, 0]
    else:
        answer = [-max_heap[0], min_heap[0]]
    return answer

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333", "D -1"]))