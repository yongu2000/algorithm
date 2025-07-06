# https://school.programmers.co.kr/learn/courses/30/lessons/70129

def solution(s):
    count = 0
    zero = 0
    while s != "1":
        count += 1
        zero += s.count("0")
        s = s.replace("0", "")
        s = str(bin(len(s)))[2:]

    print(count, zero)
    return [count, zero]

print(solution("110010101001"))
print(solution("01110"))
print(solution("1111111"))



