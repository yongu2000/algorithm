from collections import deque

def check(string):
    stack = deque()
    for s in string:
        if not stack:
            stack.append(s)
        elif stack[-1] == "[" and s == "]":
            stack.pop()
        elif stack[-1] == "{" and s == "}":
            stack.pop()
        elif stack[-1] == "(" and s == ")":
            stack.pop()
        else:
            stack.append(s)
    if not stack:
        return 1
    return 0

def push(string):
    return string[1:] + string[0]
    
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        answer += check(s)
        s = push(s)
    
    return answer