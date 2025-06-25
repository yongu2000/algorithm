# https://school.programmers.co.kr/learn/courses/30/lessons/64062

def solution(stones, k):
    answer = 0

    left = 1
    right = max(stones)

    while left <= right:
        mid = (left + right) // 2

        continuous = 0
        for stone in stones:
            if stone <= mid:
                continuous += 1
            else:
                continuous = 0

            if continuous == k:
                break

        if continuous == k:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer

print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)) # 3