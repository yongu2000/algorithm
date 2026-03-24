from collections import defaultdict

def divide(str):
    temp = defaultdict(int)
    for i in range(len(str)-1):
        if str[i].isalpha() and str[i+1].isalpha():
            temp[str[i] + str[i+1]] += 1
    return temp

def intersect(s1, s2):
    result = 0
    
    counted = set()
    
    for key, val in s1.items():
        result += min(s2[key], val)
        counted.add(key)
    
    for key, val in s2.items():
        if key not in counted:
            result += min(s1[key], val)
    
    return result

def union(s1, s2):
    result = 0
    
    counted = set()
    
    for key, val in s1.items():
        result += max(s2[key], val)
        counted.add(key)
    
    for key, val in s2.items():
        if key not in counted:
            result += max(s1[key], val)
    
    return result

def solution(str1, str2):
    answer = 0
    
    set1 = divide(str1.lower())
    set2 = divide(str2.lower())
    
    i = intersect(set1, set2)
    u = union(set1, set2)
    
    if i == 0 and u == 0:
        return 65536
    return int((i/u)*65536)