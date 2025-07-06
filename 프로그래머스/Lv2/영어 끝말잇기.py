# https://school.programmers.co.kr/learn/courses/30/lessons/12953
from collections import defaultdict
def solution(arr):
    answer = 1
    count = defaultdict(int)
    def prime_numbers(n):
        arr = [i for i in range(n+1)]
        end = int(n**(1/2))
        for i in range(2, end+1):
            if arr[i] == 0: 
                continue
            for j in range(i*i, n+1, i):
                arr[j] = 0
                
        return [i for i in arr[2:] if arr[i]]
    primes = prime_numbers(100)

    for num in arr:
        for prime in primes:
            if num >= prime:
                c = 0
                while num % prime == 0:
                    num = num // prime
                    c += 1
                count[prime] = max(count[prime], c)
            if num < prime:
                break

    for key, val in count.items():
        answer *= key ** val

    return answer

print(solution([2,6,8,14])) # 168
print(solution([1,2,3])) # 6




