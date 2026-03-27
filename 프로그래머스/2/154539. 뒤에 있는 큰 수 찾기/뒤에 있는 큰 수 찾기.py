def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    for i, number in enumerate(numbers):
        while True:
            if not stack:
                stack.append([i, number])
                break
            idx, num = stack[-1]
            if num < number:
                stack.pop()
                answer[idx] = number
            else:
                stack.append([i, number])
                break
    return answer