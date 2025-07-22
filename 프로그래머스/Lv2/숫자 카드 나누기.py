# https://school.programmers.co.kr/learn/courses/30/lessons/389479
import math

def solution(arrayA, arrayB):
    gcd = [0, 0]
    for i in range(len(arrayA)):
        gcd[0] = math.gcd(arrayA[i], gcd[0])
        gcd[1] = math.gcd(arrayB[i], gcd[1])

    for i in range(len(arrayA)):
        if arrayA[i] % gcd[1] == 0:
            gcd[1] = 1
        if arrayB[i] % gcd[0] == 0:
            gcd[0] = 1

    if gcd[0] == 1 and gcd[1] == 1:
        return 0
    else:
        return max(gcd)

print(solution([10, 17]	, 	[5, 20])) # 0
print(solution([10, 20]	, 	[5, 17])) # 10
print(solution([14, 35, 119]		, 	[18, 30, 102])) # 7













