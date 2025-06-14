# https://school.programmers.co.kr/learn/courses/30/lessons/86491


def solution(sizes):
    return max(max(w, h) for w, h in sizes) * max(min(w, h) for w, h in sizes)

print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))

