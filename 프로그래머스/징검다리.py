# https://school.programmers.co.kr/learn/courses/30/lessons/43236


def solution(distance, rocks, n):
    answer = 0

    rocks.append(distance)
    rocks.sort()

    left = 0
    right = distance

    while left <= right:
        mid = (left + right) // 2

        position = 0
        removed = 0
        for rock in rocks:
            if rock - position < mid:
                removed += 1
            else:
                position = rock
        
        if removed <= n:
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer

print(solution(25, [2, 14, 11, 21, 17], 2))