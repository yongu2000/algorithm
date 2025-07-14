# https://school.programmers.co.kr/learn/courses/30/lessons/131704

def solution(order):
    answer = 0
    n = len(order)
    order = list(reversed(order))
    storage = []

    for i in range(1, n+1):
        if order and i == order[-1]:
            order.pop()
            answer += 1
        else:
            storage.append(i)

        while storage and order and storage[-1] == order[-1]:
            storage.pop()
            order.pop()
            answer += 1
    return answer

print(solution([4, 3, 1, 2, 5]))
print(solution([5, 4, 3, 2, 1]))



