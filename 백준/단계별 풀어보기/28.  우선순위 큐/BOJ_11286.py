from queue import PriorityQueue
import sys
input = sys.stdin.readline

n = int(input())
pq = PriorityQueue()

for _ in range(n):
    i = int(input())
    if pq.empty() and i == 0:
        print(0)
    elif i != 0:
        pq.put((abs(i), i))
    else:
        print(pq.get()[1])