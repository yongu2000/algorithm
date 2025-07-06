# https://school.programmers.co.kr/learn/courses/30/lessons/152995

def solution(scores):
    answer = -1
    target_a, target_b = scores[0]
    target = sum(scores[0])

    scores.sort(key=lambda x: (-x[0], x[1]))
    max_b = -1

    print(scores)
    for a, b in scores:
        if target_a < a and target_b < b:
            answer = -1
            break
        if b >= max_b:
            max_b = b
            if a + b > target:
                answer += 1

    return answer + 1

# print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]])) 
# print(solution([[2,1],[2,2],[2,3],[3,1]])) 
print(solution([[4, 0], [2, 3], [4, 4], [2, 6]])) 

