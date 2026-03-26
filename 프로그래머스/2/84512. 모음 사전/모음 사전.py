def solution(word):
    answer = 0
    vowels = "AEIOU"
    skip = []
    for i in range(5):
        temp = 1
        for j in range(1, i+1):
            temp += 5**j
        skip.append(temp)
        
    skip = skip[::-1]
    
    for i, w in enumerate(word):
        index = vowels.find(w)
        answer += index * skip[i] + 1;
    print(skip)
    return answer