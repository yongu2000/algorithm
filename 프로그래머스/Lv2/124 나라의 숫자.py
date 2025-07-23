# https://school.programmers.co.kr/learn/courses/30/lessons/12899
def solution(n):
    answer = ''
    while n:
        n, remainder = divmod(n, 3)
        if remainder == 0:
            n -= 1
            remainder = 4
        answer = str(remainder) + answer
    
    return answer

print(solution(1)) # 1
print(solution(4)) # 11
print(solution(20)) # 11
print(solution(39)) # 11















