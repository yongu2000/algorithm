# https://school.programmers.co.kr/learn/courses/30/lessons/17677
import re, bisect

def solution(str1, str2):

    str1_list = []
    str2_list = []
    for i in range(len(str1)-1):
        if re.match("[a-z]", str1[i].lower()) and re.match("[a-z]", str1[i+1].lower()):
            str1_list.append(str1[i].lower() + str1[i+1].lower())

    for i in range(len(str2)-1):
        if re.match("[a-z]", str2[i].lower()) and re.match("[a-z]", str2[i+1].lower()):
            str2_list.append(str2[i].lower() + str2[i+1].lower())
    
    str1_list.sort()
    str2_list.sort()

    intersect = 0
    union = 0
    counted = set()
    for i in str1_list:
        if i not in counted:
            count1 =  bisect.bisect_right(str1_list, i) - bisect.bisect_left(str1_list, i)
            count2 =  bisect.bisect_right(str2_list, i) - bisect.bisect_left(str2_list, i)
            intersect += min(count1, count2)
            union += max(count1, count2)
            counted.add(i)

    for i in str2_list:
        if i not in counted:
            count1 =  bisect.bisect_right(str1_list, i) - bisect.bisect_left(str1_list, i)
            count2 =  bisect.bisect_right(str2_list, i) - bisect.bisect_left(str2_list, i)

            union += max(count1, count2)
            counted.add(i)
    
    if intersect == 0 and union == 0:
        return 65536
    return int((intersect / union) * 65536)


print(solution("ABAB", "BABA")) #  32768 









