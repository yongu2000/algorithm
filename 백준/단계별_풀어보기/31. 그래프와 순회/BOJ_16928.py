import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    queue = deque()
    queue.append(1)
    
    while queue:
        pos = queue.popleft()
        if pos == 100:
            return
        
        for i in range(1, 7):
            n_pos = pos + i
            if n_pos in ladders.keys():
                n_pos = ladders[n_pos]
            if n_pos in snakes.keys():
                n_pos = snakes[n_pos]

            if 0 <= n_pos <= 100 and board[n_pos] == 0:
                queue.append(n_pos)
                board[n_pos] = board[pos] + 1       


n, m = map(int, input().split())
board = [0] * 101
ladders = dict()
snakes = dict()
for _ in range(n):
    start, end = map(int, input().split())
    ladders[start] = end

for _ in range(m):
    start, end = map(int, input().split())
    snakes[start] = end
bfs()
print(board[100])