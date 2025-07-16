# https://school.programmers.co.kr/learn/courses/30/lessons/77885

def solution(numbers):
    answer = []
    for num in numbers:
        standard = list(reversed(list('0' + bin(num)[2:])))
        for idx, val in enumerate(standard):
            if val == '0':
                if idx > 0:
                    standard[idx-1] = '0'
                standard[idx] = '1'
                break
        answer.append(int(''.join(list(reversed(standard))),2))
            
    return answer

print(solution([2,7])) # 5



