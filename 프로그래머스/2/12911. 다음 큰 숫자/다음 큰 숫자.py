def solution(n):
    ones = str(bin(n)[2:]).count('1')
    while True:
        n += 1
        next = str(bin(n)[2:]).count('1')
        
        if next == ones:
            return n
