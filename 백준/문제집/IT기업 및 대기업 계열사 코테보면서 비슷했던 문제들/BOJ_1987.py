import sys
from collections import defaultdict
input = sys.stdin.readline

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def dfs(x, y, dist):
    global answer
    
    answer = max(answer, dist)
    
    alphabets[board[x][y]] = 1
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < r and 0 <= ny < c and alphabets[board[nx][ny]] == 0:
            dfs(nx, ny, dist+1)
    
    alphabets[board[x][y]] = 0

r, c = map(int, input().split())
board = [list(input().strip()) for _ in range(r)]
alphabets = defaultdict(int)

answer = -1

dfs(0, 0, 1)

print(answer)