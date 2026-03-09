def solution(n):
    answer = 0
    left = 1
    right = 1
    
    temp = 1
    while (right <= n):
        if temp < n:
            right += 1
            temp += right
        elif temp > n:
            temp -= left
            left += 1
        else:
            answer += 1
            right += 1
            temp += right
            
    return answer