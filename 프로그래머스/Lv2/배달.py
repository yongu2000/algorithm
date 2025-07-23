# https://school.programmers.co.kr/learn/courses/30/lessons/12978
from heapq import heappush, heappop

def solution(N, road, K):
    answer = 0
    INF = 1000000000

    graph = [[] for _ in range(N+1)]
    distance = [INF]*(N+1)

    for s, e, w in road:
        graph[s].append([e, w])
        graph[e].append([s, w])
    
    queue = []
    heappush(queue, (0, 1))
    distance[1] = 0

    while queue:
        w1, u = heappop(queue)

        for v, w2 in graph[u]:
            cost = distance[u] + w2
            if cost < distance[v]:
                distance[v] = cost
                heappush(queue, (cost, v))

    for d in distance:
        if d <= K:
            answer += 1
    return answer

print(solution(5, 	[[1,2,1],[2,3,3],[5,2,2],[1,4,2],[5,3,1],[5,4,2]], 3)) # 4
print(solution(6, 	[[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4)) # 4













