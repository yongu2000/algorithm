from collections import deque
def solution(people, limit):
    answer = 0
    people.sort()
    
    p = deque(people)
    
    while len(p) > 0:
        if len(p) == 1:
            answer += 1
            p.pop()
        elif p[0] + p[-1] > limit:
            answer += 1
            p.pop()
        else:
            p.popleft()
            p.pop()
            answer += 1
    
    return answer