# https://school.programmers.co.kr/learn/courses/30/lessons/389479
from collections import deque

def solution(players, m, k):
    answer = 0
    server = deque([0]*k)
    for player in players:
        s = server.popleft() + 1
        server.append(0)
        if player >= s*m:
            answer += (player // m) - s + 1
            for i in range(k-1):
                server[i] += (player // m) - s + 1

    return answer

print(solution([2, 2]	, 1, 1)) # 4












