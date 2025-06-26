# https://school.programmers.co.kr/learn/courses/30/lessons/67259

from collections import deque

dx = [1,0,-1,0]
dy = [0,1,0,-1]
MAX = 987654321
answer = MAX

def solution(board):
    global answer
    answer = MAX
    visited = [[[MAX for y in range(len(board))] for x in range(len(board))] for z in range(4)]
    print(visited)

    def bfs():
        queue = deque()
        if board[0][1] != 1:
            queue.append([0,1,100,1])
            visited[1][0][1] = 100
        if board[1][0] != 1:
            queue.append([1,0,100,0])
            visited[0][1][0] = 100

        while queue:
            x, y, cost, dir = queue.pop()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if dir != i:
                    n_cost = cost + 600
                else:
                    n_cost = cost + 100

                if 0 <= nx < len(board) and 0 <= ny < len(board):
                    if board[nx][ny] != 1:
                        if visited[i][nx][ny] > n_cost:
                            queue.append([nx, ny, n_cost, i])
                            visited[i][nx][ny] = n_cost
        
    for z in range(4):
        visited[z][0][0] = 0
        
    bfs()

    for z in range(4):
        if answer > visited[z][len(board)-1][len(board)-1]:
            answer = visited[z][len(board)-1][len(board)-1]

    return answer

print(solution([[0,0,0],[0,0,0],[0,0,0]]))
print(solution([[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]))
print(solution([[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]))
print(solution([[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]]))
