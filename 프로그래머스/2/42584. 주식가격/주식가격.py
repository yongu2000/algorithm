from collections import deque
def solution(prices):
    answer = [0] * len(prices)
    
    data = deque()
    for i, val in enumerate(prices):
        data.append([i, val])
    stack = []
    
    while data:
        idx, num = data.popleft()

        while stack and stack[-1][1] > num:
            i, v = stack.pop()
            answer[i] = idx - i
        stack.append([idx, num])
        
    while stack:
        idx, num = stack.pop()
        answer[idx] = len(prices) - idx - 1
        
    return answer