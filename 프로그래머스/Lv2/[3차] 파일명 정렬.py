# https://school.programmers.co.kr/learn/courses/30/lessons/17686

import re

def solution(files):
    answer = []
    sort_list = []

    for idx, file in enumerate(files):
        head = ''
        number = ''
        tail = ''

        head_flag = True
        number_flag = True
        for f in file:
            if number_flag and re.match("[0-9]", f):
                head_flag = False
                number += f
            elif head_flag:
                head += f
            else:
                number_flag = False
                tail += f
        
        sort_list.append([head.lower(), int(number), tail, idx])
    sort_list.sort(key=lambda x: (x[0], x[1], x[3]))

    for item in sort_list:
        answer.append(files[item[3]])
    return answer

print(solution(["img12.png", "img10.png", "img02.png", "img1s2.png", "IMG01.GIF", "img2.JPG"])) # 5
print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])) # 5



