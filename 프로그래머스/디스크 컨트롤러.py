# https://school.programmers.co.kr/learn/courses/30/lessons/12979


from heapq import heappop, heappush
def solution(jobs):
    queue = []

    jobs.sort(reverse=True)
    n = len(jobs)
    elasped = 0
    count = 0
    answer = 0

    while count < n:
        while jobs and jobs[-1][0] <= elasped:
            start, duration = jobs.pop()
            heappush(queue, [duration, start])

        if not queue:
            start, duration = jobs.pop()
            heappush(queue, [duration, start])
            elasped = start
        
        duration, start = heappop(queue)
        elasped += duration
        answer += elasped - start
                
        count += 1

    answer /= n

    return int(answer)
print(solution([[0, 3], [1, 9], [3, 5]]))
print(solution([[2, 3], [3, 9], [3, 5]]))
print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[0, 20], [1, 10], [2, 6]]))

# print(solution([[0, 3], [1, 9], [2, 6]]))






