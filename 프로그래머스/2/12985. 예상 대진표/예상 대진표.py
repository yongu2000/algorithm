def solution(n,a,b):
    answer = 1
    a = a-1
    b = b-1
    while True:
        if a//2 == b//2 or (a == 0 and b == 1) or (a == 1 and b == 0):
            return answer
        else:
            answer += 1
            a = a //2
            b = b // 2
