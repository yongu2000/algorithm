# https://school.programmers.co.kr/learn/courses/30/lessons/132266
from collections import deque

def solution(n, roads, sources, destination):
    answer = []

    data = [[] for _ in range(n+1)]

    for road in roads:
        start, end = road
        data[start].append(end)
        data[end].append(start)

    costs = [-1] * (n+1)

    def bfs(destination):
        queue = deque()
        visited = [False] * (n+1)
        
        queue.append([destination, 0])
        visited[destination] = True

        while queue:
            area, count = queue.popleft()
            costs[area] = count
            for next in data[area]:
                if not visited[next]:
                    queue.append([next, count+1])
                    visited[next] = True
    
    bfs(destination)

    for source in sources:
        answer.append(costs[source])

    return answer


print(solution(3, [[1, 2], [2, 3]], [2, 3], 1))
print(solution(5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5))

