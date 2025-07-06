# https://school.programmers.co.kr/learn/courses/30/lessons/12973

def solution(s):
    stack = [s[0]]
    for i in range(1, len(s)):
        stack.pop() if stack and stack[-1] == s[i] else stack.append(s[i])
    return 0 if stack else 1


print(solution("baabaa"))
print(solution("cdcd"))



