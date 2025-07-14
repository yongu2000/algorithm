# https://school.programmers.co.kr/learn/courses/30/lessons/154538
from collections import deque

def solution(x, y, n):
    answer = -1
    visited = [False] * (y+1)
    queue = deque()
    queue.append([x, 0])
    visited[x] = True

    while queue:
        num, cnt = queue.popleft()

        if num == y:
            return cnt
        if num + n <= y and not visited[num+n]:
            queue.append([num + n, cnt+1])
            visited[num + n] = True    

        if num * 2 <= y and not visited[num*2]:
            queue.append([num*2, cnt+1])
            visited[num*2] = True    

        if num * 3 <= y and not visited[num*3]:
            queue.append([num*3, cnt+1])
            visited[num*3] = True    

    return answer

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))



