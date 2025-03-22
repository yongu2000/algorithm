# import sys
# import heapq
# input = sys.stdin.readline

# n = int(input())
# queue = []
# for i in range(n):
#     heapq.heappush(queue, int(input()))
#     print(sorted(queue)[i//2])
# n^2 log n 시간초과 


import sys
import heapq

input = sys.stdin.readline

n = int(input())
max_heap = []
min_heap = []

for i in range(n):
    num = int(input())

    if not max_heap or num <= -max_heap[0]:
        heapq.heappush(max_heap, -num)
    else:
        heapq.heappush(min_heap, num)

    if len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    elif len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))

    print(-max_heap[0])
