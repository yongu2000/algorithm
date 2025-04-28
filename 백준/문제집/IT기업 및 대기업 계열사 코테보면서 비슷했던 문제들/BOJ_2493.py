import sys, heapq
input = sys.stdin.readline

n = int(input())

tower = list(map(int, input().split()))

heap = []
answer = {}
for i in range(n, 0, -1):
    t = tower[i-1]
    if heap:
        while heap and heap[0] < t:
            answer[heapq.heappop(heap)] = i
    heapq.heappush(heap, t)
for h in heap:
    answer[h] = 0
print(*[answer[t] for t in tower])