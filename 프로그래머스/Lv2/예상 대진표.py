# https://school.programmers.co.kr/learn/courses/30/lessons/12985

def solution(n,a,b):
    answer = 0
    while n >= 1:
        answer += 1
        a = (a+1) // 2
        b = (b+1) // 2
        if a == b:
            break
        n = n // 2
    return answer

print(solution(8, 4, 7)) # 3




