def solution(msg):
    answer = []
    dictionary = dict()
    idx = 1
    for i in range(ord("A"), ord("Z")+1):
        dictionary[chr(i)] = idx
        idx += 1
        
    i = 0
    while i < len(msg):
        temp = ""
        for j in range(i, len(msg)):
            temp += msg[j]
            if temp not in dictionary:
                answer.append(dictionary[temp[:-1]])
                dictionary[temp] = idx
                idx += 1
                i = j - 1
                break
            
            if j == len(msg)-1:
                answer.append(dictionary[temp])
                i = j
                break
        i += 1
    
    return answer