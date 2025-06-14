# https://school.programmers.co.kr/learn/courses/30/lessons/42842


def solution(brown, yellow):
    
    possible = []
    for i in range(1, brown + yellow + 1):
        if (brown + yellow) % i == 0 and i >= (brown + yellow) // i:
            possible.append([i, (brown + yellow) // i])

    for p in possible:
        w, l = p
        if w*2 + l*2 - 4 == brown:
            return p

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))

