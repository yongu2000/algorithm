import sys, heapq
input = sys.stdin.readline

n = int(input())

pq = []
for _ in range(n):
    for val in list(map(int, input().split())):
        if len(pq) < n:
            heapq.heappush(pq, val)
        elif val > pq[0]:
            heapq.heappop(pq)
            heapq.heappush(pq, val)
print(pq[0])