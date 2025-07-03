# https://school.programmers.co.kr/learn/courses/30/lessons/49191
from collections import deque

def solution(n, results):
    answer = 0
    win = [[] for _ in range(n+1)]
    lose = [[] for _ in range(n+1)]

    for r in results:
        winner, loser = r
        win[loser].append(winner)
        lose[winner].append(loser)
    
    for i in range(1, n+1):
        visited = [False] * (n+1)
        count = 0
        q = deque()
        q.append(i)
        visited[i] = True
        while q:
            node = q.popleft()
            for next in win[node]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    count += 1
        
        q = deque()
        q.append(i)
        visited[i] = True
        while q:
            node = q.popleft()
            for next in lose[node]:
                if not visited[next]:
                    q.append(next)
                    visited[next] = True
                    count += 1
        
        if count == n-1:
            answer +=1
    
    return answer

print(solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]])) # 2