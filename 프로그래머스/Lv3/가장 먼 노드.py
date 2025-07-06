# https://school.programmers.co.kr/learn/courses/30/lessons/49189

from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(n+1)]
    distance = [0] * (n+1)
    visited = [False] * (n+1)

    for e in edge:
        start, end = e
        graph[start].append(end)
        graph[end].append(start)
    
    
    queue = deque()
    queue.append([1, 0])
    visited[1] = True
    
    while queue:
        node, dist = queue.popleft()
        distance[node] = dist+1

        for next in graph[node]:
            if not visited[next]:
                visited[next] = True
                queue.append([next, dist+1])
    
    max_dist = max(distance)
    return distance.count(max_dist)

print(solution(6, 	[[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]	)) # 3












