# https://school.programmers.co.kr/learn/courses/30/lessons/84512

def dfs(word):
    global count
    if len(word) == 5:
        return
    for i in range(5):
        word += vowels[i]
        dictionary[word] = count
        count += 1
        dfs(word)
        word = word[:-1]   

vowels = ["A", "E", "I", "O", "U"]
dictionary = dict()
count = 1
dfs("")

def solution(word):
    return dictionary[word]

print(solution("AAAAE"))
print(solution("AAAE"))
print(solution("I"))
print(solution("EIO"))

