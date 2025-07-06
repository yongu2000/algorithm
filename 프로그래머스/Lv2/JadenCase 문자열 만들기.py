# https://school.programmers.co.kr/learn/courses/30/lessons/12951
import re

def solution(s):
    first = True
    answer = ''
    for string in list(s.lower()):
        if first and re.match("[a-z]", string):
            answer += string.upper()
            first = False
            continue
        else:
            first = False
        if string == ' ':
            first = True
        answer += string
    return answer

print(solution("3people unFollowed me"))
print(solution("for the last week"))
print(solution(" FOR  1HE 2ast week   "))



