# https://school.programmers.co.kr/learn/courses/30/lessons/148653

def solution(storey):
    answer = 0
    storey = list(map(int, str(storey)[::-1]))

    for idx, num in enumerate(storey):
        if num < 5:
            answer += num
        elif num == 5:
            answer += 5
            if idx < len(storey) - 1 and storey[idx+1] >= 5:
                storey[idx+1] += 1
        else:
            answer += 10 - num
            if idx == len(storey) - 1:
                storey.append(1)
            else:
                storey[idx+1] += 1

    return answer

print(solution(45 )) # 9
print(solution(95  )) # 6
