# https://school.programmers.co.kr/learn/courses/30/lessons/76502

def solution(s):
    answer = 0
    
    for i in range(len(s)):
        stack = []
        for j in range(len(s)):
            idx = j+i
            if idx >= len(s):
                idx = (j+i) % len(s)

            if not stack:
                stack.append(s[idx])
            elif s[idx] == "]" and stack[-1] == "[":
                stack.pop()
            elif s[idx] == ")" and stack[-1] == "(":
                stack.pop()
            elif s[idx] == "}" and stack[-1] == "{":
                stack.pop()
            else:
                stack.append(s[idx])
        if not stack:
            answer += 1    

    return answer


print(solution("[](){}")) # 3
print(solution("}]()[{")) # 2
print(solution("[)(]")) # 0
print(solution("}}}")) # 0





