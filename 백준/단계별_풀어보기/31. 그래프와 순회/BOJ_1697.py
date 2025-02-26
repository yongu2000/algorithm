import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(n)
    data[n] = 1
    while queue:
        num = queue.popleft()

        if num == k:
            return data[num]
        
        a = num - 1
        b = num + 1
        c = num * 2

        if 0 <= a <= 100_000 and data[a] == 0:
            data[a] = data[num]+1
            queue.append(a)
        if 0 <= b <= 100_000 and data[b] == 0:
            data[b] = data[num]+1
            queue.append(b)
        if 0 <= c <= 100_000 and data[c] == 0:
            data[c] = data[num]+1
            queue.append(c)
    return 

n, k = map(int, input().split())

data = [0] * 100_001
bfs()
print(data[k] - 1)
