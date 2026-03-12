def solution(n):
    result = [0] * (n+1)
    if n == 1:
        return 1
    elif n == 2:
        return 2
    result[1] = 1
    result[2] = 2
    
    for i in range(3, n+1):
        result[i] = result[i-1] % 1234567 + result[i-2] % 1234567
    return result[n] % 1234567