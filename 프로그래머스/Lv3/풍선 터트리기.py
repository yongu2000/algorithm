# https://school.programmers.co.kr/learn/courses/30/lessons/68646

def solution(a):
    answer = 0
    n = len(a)
    MAX = 1_000_000_000

    left = [MAX] * n
    right = [MAX] * n
    
    left_min = MAX
    for i in range(n):
        balloon = a[i]
        if balloon < left_min:
            left_min = balloon
        left[i] = left_min

    right_min = MAX
    for i in range(n-1, -1, -1):
        balloon = a[i]
        if balloon < right_min:
            right_min = balloon
        right[i] = right_min

    for i in range(n):
        count = 0
        if left[i] < a[i]:
            count += 1
        if right[i] < a[i]:
            count += 1

        if count < 2:
            answer += 1

    return answer


print(solution([1])) # 1
print(solution([1, 2])) # 2
print(solution([9, -1, -5])) # 3
print(solution([-16,27,65,-2,58,-92,-71,-68,-61,-33])) # 6
