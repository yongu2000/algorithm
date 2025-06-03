import sys
from bisect import bisect_right
input = sys.stdin.readline

n, h = map(int, input().split())
obstacles = [int(input()) for _ in range(n)]

up = [0]*(h+1)
down = [0]*(h+1)

for idx, val in enumerate(obstacles):
    if idx % 2 != 0:
        down[val] += 1
    else:
        up[val] += 1

for i in range(h-1,0,-1):
    up[i] += up[i+1]
    down[i] += down[i+1]

counts = []
for i in range(1, h+1):
    counts.append(up[i] + down[-i])
counts.sort()
print(min(counts), bisect_right(counts, min(counts)))