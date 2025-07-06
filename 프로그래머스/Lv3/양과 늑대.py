# https://school.programmers.co.kr/learn/courses/30/lessons/92343
answer = 1

def solution(info, edges):
    global answer
    answer = 1
    n = len(info)
    sheep = 0
    for i in info:
        if i == 0:
            sheep += 1

    visited = [[False] * n for _ in range(sheep+1)]
    graph = [[] for _ in range(n)]
    for start, end in edges:
        graph[start].append(end)
        graph[end].append(start)

    def dfs(node, cur_sheep, cur_wolf):
        global answer
        answer = max(answer, cur_sheep)
        if cur_sheep == sheep:
            return
        
        for next in graph[node]:
            if info[next] == 0 and not visited[cur_sheep+1][next]:
                visited[cur_sheep+1][next] = True
                info[next] = -1
                dfs(next, cur_sheep + 1, cur_wolf)
                info[next] = 0
                visited[cur_sheep+1][next] = False
            elif info[next] == 1:
                if cur_sheep > cur_wolf + 1 and not visited[cur_sheep][next]:
                    visited[cur_sheep][next] = True
                    info[next] = -1
                    dfs(next, cur_sheep, cur_wolf + 1)
                    info[next] = 1
                    visited[cur_sheep][next] = False
            else:
                if not visited[cur_sheep][next]:
                    visited[cur_sheep][next] = True
                    dfs(next, cur_sheep, cur_wolf)
                    visited[cur_sheep][next] = False
    info[0] = -1
    dfs(0, 1, 0)
    return answer

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]
               )) # 5
print(solution([0,1,0,1,1,0,1,0,0,1,0], [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]
               )) # 5
print(solution([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [4, 10], [5, 11], [5, 12], [6, 13], [6, 14], [7, 15], [7, 16]]
               )) # 5

