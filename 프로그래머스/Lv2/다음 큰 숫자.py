# https://school.programmers.co.kr/learn/courses/30/lessons/12911

def solution(n):
    one = str(bin(n)[2:]).count("1")
    for i in range(n+1, 1_000_000):
        if str(bin(i)[2:]).count("1") == one:
            return i


print(solution(78))
print(solution(15))



