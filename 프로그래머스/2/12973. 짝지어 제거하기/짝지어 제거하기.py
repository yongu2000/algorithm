from collections import deque

def solution(s):
    
    stack = deque()
    for char in s:
        if len(stack) == 0:
            stack.append(char)
        elif stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
        
    if len(stack) == 0:
        return 1
    else:
        return 0
