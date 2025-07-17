# https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = []
    snail = [[0]*n for _ in range(n)]
    dx = [1, 0, -1]
    dy = [0, 1, -1]

    num = 1
    x = 0
    y = 0
    d = 0
    while True:
        snail[x][y] = num
        num += 1
        nx = x + dx[d]
        ny = y + dy[d]

        if nx == n or ny ==n or snail[nx][ny] != 0:
            d = (d+1) % 3
            nx = x + dx[d]
            ny = y + dy[d]
            if nx == n or ny ==n or snail[nx][ny] != 0:
                break
        x = nx
        y = ny

    for i in range(n):
        for j in range(i+1):
            answer.append(snail[i][j])

    return answer


print(solution(4)) # [1,2,9,3,10,8,4,5,6,7]
print(solution(5)) # 	[1,2,12,3,13,11,4,14,15,10,5,6,7,8,9]
print(solution(6)) # [1,2,15,3,16,14,4,17,21,13,5,18,19,20,12,6,7,8,9,10,11]


