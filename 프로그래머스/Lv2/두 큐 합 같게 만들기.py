# https://school.programmers.co.kr/learn/courses/30/lessons/118667

def solution(queue1, queue2):
    answer = -1
    target = (sum(queue1) + sum(queue2)) // 2
    
    queue = queue1 + queue2

    left = 0
    right = len(queue1)-1

    sums = sum(queue1)
    cnt  = 0
    while left <= right and right < len(queue)-1:
        if sums < target:
            right += 1
            sums += queue[right]
            cnt += 1
        elif sums > target:
            sums -= queue[left]
            left += 1
            cnt += 1
        else:
            return cnt
    return answer


print(solution([3, 2, 7, 2],[4, 6, 5, 1]		)) # 2
print(solution([1, 2, 1, 2]	,[1, 10, 1, 2])) # 7
print(solution([1, 1]	,[1, 5])) # -1


