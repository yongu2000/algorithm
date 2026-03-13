def solution(n, left, right):
    
    arr = []
    for i in range(left-1, right):
        arr.append(((i+1) // n) + 1 if (((i+1) % n) + 1 < ((i+1) // n) + 1) else ((i+1) % n) + 1)
    
    return arr