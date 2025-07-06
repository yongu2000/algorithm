# https://school.programmers.co.kr/learn/courses/30/lessons/43163

alphabets = ["a", "b", "c", "d", "e", "f", 
             "g", "h", "i", "j", "k", "l", 
             "m", "n", "o", "p", "q", "r", 
             "s", "t", "u", "v", "w", "x",
             "y", "z"]

from collections import deque


def solution(begin, target, words):
    answer = 0
    words = set(words)
    visited = set()
    queue = deque()
    queue.append([begin, 0])

    while queue:
        word, count = queue.popleft()
        if word == target:
            answer = count
            break
        
        for i in range(len(word)):
            for a in alphabets:
                new_word = word[:i] + a + word[i+1:]

                if new_word in words and new_word not in visited:
                    visited.add(new_word)
                    queue.append([new_word, count+1])

    return answer

print(solution("hit", "cog",  ["hot", "dot", "dog", "lot", "log"]))