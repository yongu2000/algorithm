# https://school.programmers.co.kr/learn/courses/30/lessons/42861

from heapq import heappush, heappop

def solution(n, costs):
    answer = 0

    visited = [False] * n
    islands = [[] for _ in range(n)]

    for cost in costs:
        start, end, val = cost
        islands[start].append([end, val])
        islands[end].append([start, val])

    queue = []
    queue.append([0, 0])

    while queue:
        cost, node = heappop(queue)
        
        if not visited[node]:
            visited[node] = True

            answer += cost
            for next in islands[node]:
                next_node, next_cost = next
                if not visited[next_node]:
                    heappush(queue, [next_cost, next_node])

    return answer

print(solution(4, [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]])) # 4