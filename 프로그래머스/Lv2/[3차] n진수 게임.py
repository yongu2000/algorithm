# https://school.programmers.co.kr/learn/courses/30/lessons/17687


def solution(n, t, m, p):
    digit_dict = dict()
    digit_dict[10] = "A"
    digit_dict[11] = "B"
    digit_dict[12] = "C"
    digit_dict[13] = "D"
    digit_dict[14] = "E"
    digit_dict[15] = "F"

    def convert_digit(num, n):
        result = ''
        if num == 0:
            return '0'
        while num != 0:
            result +=  str(digit_dict[num%n]) if n > 10 and num%n >= 10 else str(num%n)
            num = num // n
        return result[::-1]
    
    game = ''
    num = 0
    while len(game) <= t*m:
        game += convert_digit(num, n)
        num += 1

    answer = ''
    for idx, val in enumerate(game):
        if (idx+1) % m == p % m:
            answer += val 
        if len(answer) == t:
            break

    return answer

print(solution(2, 4, 2, 1))
print(solution(16, 16, 2, 1))
print(solution(16, 16, 2, 2))



