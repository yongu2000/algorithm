# https://school.programmers.co.kr/learn/courses/30/lessons/12938

# 원소의 곱이 최대가 되는 집합은 평균으로 이루어진 집합

def solution(n, s):
    if n > s:
        return [-1]
    # 평균으로 나누어떨어지지 않으면 나머지만큼 1 더한 값 추가
    return [s//n for _ in range(n - s%n)] + [s//n + 1 for _ in range(s%n)]

print(solution(2, 9))
print(solution(2, 1))
print(solution(2, 8))
print(solution(10, 33))

