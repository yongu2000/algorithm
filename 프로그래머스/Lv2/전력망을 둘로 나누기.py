# https://school.programmers.co.kr/learn/courses/30/lessons/86971
from collections import deque

towers = []
visited = []
answer = -1

def bfs(start, wire):
    queue = deque()
    if visited[start]:
        return
    queue.append(start)
    visited[start] = True
    count = 1
    while queue:
        node = queue.popleft()

        for next in towers[node]:
            if [node, next] != wire and [next, node] != wire and not visited[next]:
                queue.append(next)
                visited[next] = True
                count += 1    
    return count

def solution(n, wires):
    global answer, visited, towers
    answer = 101
    towers = [[] for _ in range(n+1)]

    for wire in wires:
        start, end = wire
        towers[start].append(end)
        towers[end].append(start)

    for wire in wires:
        visited = [False] * (n+1)
        temp = []
        for i in range(n):
            if not visited[i+1]:
                temp.append(bfs(i+1, wire))
        print(temp)
        answer = min(answer, abs(temp[0] - temp[1]))

    return answer

print(solution(9, 	[[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))
print(solution(4, 	[[1, 2], [2, 3], [3, 4]]))
print(solution(7, 	[[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))


