import sys
from collections import defaultdict
input = sys.stdin.readline

n, k = map(int, input().split())

sequence = list(map(int, input().split()))

data = defaultdict(int)
p1, p2 = 0, 0
answer = 0
while p2 < n:
    if data[sequence[p2]] >= k:
        data[sequence[p1]] -= 1
        p1 += 1
    else:
        data[sequence[p2]] += 1
        p2 += 1
        answer = max(answer, p2 - p1)
print(answer)