data = {10 : "A", 11: "B", 12:"C", 13:"D", 14:"E", 15:"F"}

def convert(n, q):
    rev_base = []

    while n > 0:
        n, mod = divmod(n, q)
        if mod >= 10:
            rev_base.append(str(data[mod]))
        else : 
            rev_base.append(str(mod))
    
    if not rev_base:
        return str(0)
    
    return "".join(rev_base[::-1])
    

def solution(n, t, m, p):
    answer = ''
    num = 0   
    idx = 0    
    
    while len(answer) < t:
        converted_str = convert(num, n)
        
        for char in converted_str:
            if idx % m == p - 1:
                answer += char
                if len(answer) == t:
                    return answer
            idx += 1
        num += 1
    return answer