# https://school.programmers.co.kr/learn/courses/30/lessons/154539

def solution(numbers):
    n = len(numbers)
    answer = [0] * (n)

    stack = []
    for idx, num in enumerate(numbers):
        while stack and stack[-1][1] < num:
            i, _ = stack.pop()
            answer[i] = num
        stack.append([idx, num])
    while stack:
        i, _ = stack.pop()
        answer[i] = -1
        
    return answer

print(solution([2, 3, 3, 5]))
print(solution([9, 1, 5, 3, 6, 2]))
