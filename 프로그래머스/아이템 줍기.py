# https://school.programmers.co.kr/learn/courses/30/lessons/87694

from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0

    graph = [[0]*101 for _ in range(101)]
    visited = [[0]*101 for _ in range(101)]

    for rec in rectangle:
        rec[0] *= 2
        rec[1] *= 2
        rec[2] *= 2
        rec[3] *= 2
    characterX *= 2
    characterY *= 2
    itemX *= 2
    itemY *= 2

    for idx, rec in enumerate(rectangle):
        x1, y1, x2, y2 = rec

        for y in range(y1, y2+1):
            for x in range(x1, x2+1):
                graph[y][x] = 1

    for rec in rectangle:
        x1, y1, x2, y2 = rec

        for y in range(y1+1, y2):
            for x in range(x1+1, x2):
                graph[y][x] = 0

    queue = deque()

    visited[characterY][characterX] = True
    queue.append([characterX, characterY, 0])

    while queue:
        x, y, count = queue.popleft()

        if x == itemX and y == itemY:
            return count // 2

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 101 and 0 <= ny < 101 and not visited[ny][nx] and graph[ny][nx] != 0:
                visited[ny][nx] = True
                queue.append([nx, ny, count+1])

    return answer

print(solution([[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]], 1, 3, 7, 8))
print(solution([[1,1,8,4],[2,2,4,9],[3,6,9,8],[6,3,7,7]], 9, 7, 6, 1))
print(solution([[1, 1, 5, 7]], 1, 1, 4, 7))
print(solution([[2, 1, 7, 5], [6, 4, 10, 10]], 3, 1, 7, 10))
print(solution([[2, 2, 5, 5], [1, 3, 6, 4], [3, 1, 4, 6]], 1, 4, 6, 3))
