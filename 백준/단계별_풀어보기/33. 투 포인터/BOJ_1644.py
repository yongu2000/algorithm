import sys
input = sys.stdin.readline

def prime_numbers(n):
    arr = [i for i in range(n+1)]
    end = int(n**(1/2))
    for i in range(2, end+1):
        if arr[i] == 0: 
            continue
        for j in range(i*i, n+1, i):
            arr[j] = 0
            
    return [i for i in arr[2:] if arr[i]]

n = int(input())
primes = prime_numbers(n)
sums = [0]
for i in range(len(primes)):
    sums.append(primes[i]+sums[i])
left = 1
right = 1
answer = 0
while left <= right and right < len(sums):
    temp = sums[right] - sums[left-1]

    if temp >= n:
        if temp == n:
            answer += 1
        left += 1
    else:
        right += 1
print(answer)