import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
heights = list(map(int, input().split()))

queue = deque()
for i in range(len(heights), 0, -1):
    if not queue:
        queue.append(i)
        continue

    count = heights[i-1]
    inserted = False
    for index, val in enumerate(queue):
        if val > i:
            if count == 0:
                inserted = True
                queue.insert(index, i)
                break
            count -= 1
    if not inserted:
        queue.append(i)
print(" ".join(map(str, queue)))