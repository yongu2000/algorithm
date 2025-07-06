# https://school.programmers.co.kr/learn/courses/30/lessons/12924

def solution(n):
    answer = 0
    nums = [i for i in range(n+1)]
    sums = [0] * (n+1)

    for i in range(1, n+1):
        sums[i] = sums[i-1] + nums[i]

    left = 1
    right = 1

    while left <= right and left <= n and right <= n:
        if sums[right] - sums[left-1] >= n:
            if sums[right] - sums[left-1] == n:
                answer += 1
            left += 1
        elif sums[right] - sums[left-1] < n:
            right += 1


    return answer

print(solution(15))



