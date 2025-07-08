# https://school.programmers.co.kr/learn/courses/30/lessons/87390

def solution(n, left, right):
    answer = []

    for i in range(left, right+1):
        row, col = i // n, i % n
        num = row if row > col else col
        answer.append(num+1)

    return answer

print(solution(3, 2, 5)) # [3,2,2,3]
print(solution(4, 7, 14)) # [4,3,3,3,4,4,4,4]





