# https://school.programmers.co.kr/learn/courses/30/lessons/42839

import itertools

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: 
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

def solution(numbers):
    nums = set()
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        for j in set(itertools.permutations(list(numbers),i)):
            nums.add(int("".join(j)))
    primes = set(prime_numbers(max(nums)))
    
    for n in nums:
        if n in primes:
            answer += 1
    return answer

print(solution("17"))
print(solution("011"))

