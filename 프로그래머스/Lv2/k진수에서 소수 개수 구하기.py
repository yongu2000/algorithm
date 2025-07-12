# https://school.programmers.co.kr/learn/courses/30/lessons/92335

def convert_digit(num, n):
    result = ''
    if num == 0:
        return '0'
    while num != 0:
        result += str(num%n)
        num = num // n
    return result[::-1]

def is_prime(num):
    if num == 1:
        return False
    for i in range(2, int(num**(1/2))+1):
        if num % i == 0:
            return False
        
    return True

def solution(n, k):
    answer = 0
    converted = [int(x) for x in convert_digit(n, k).split("0") if x]

    for num in converted:
        if is_prime(num):
            answer += 1
    return answer

print(solution(797161, 3))
print(solution(437674, 3))
print(solution(110011, 10))




