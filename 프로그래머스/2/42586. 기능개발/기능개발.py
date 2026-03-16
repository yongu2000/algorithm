from collections import deque
import math

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    while progresses:
        job = 0
        day = math.ceil((100 - progresses[0]) / speeds[0])
        
        for i in range(len(progresses)):
            progresses[i] += speeds[i] * day
        
        while progresses and progresses[0] >= 100:
            progresses.popleft()
            speeds.popleft()
            job += 1
        answer.append(job)
    return answer