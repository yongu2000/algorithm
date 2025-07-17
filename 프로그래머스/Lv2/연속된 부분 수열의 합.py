# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    n = len(sequence)
    sums = [0]*(n+1)

    for i in range(n):
        sums[i+1] = sums[i] + sequence[i]
    
    left = 0
    right = 0

    while left <= right and right <= n:
        sum = sums[right] - sums[left]
        if sum < k:
            right += 1
        elif sum > k:
            left += 1
        else:
            answer.append([left, right-1])
            left += 1
    answer.sort(key=lambda x : x[1]-x[0])
    return answer[0]


print(solution([1, 2, 3, 4, 5], 7)) # [2, 3]
print(solution([1, 1, 1, 2, 3, 4, 5], 5)) # 	[6, 6]
print(solution([2, 2, 2, 2, 2], 6)) # [0, 2]


