import sys
input = sys.stdin.readline

def binary_search(num, A):
    start = 0
    end = len(A)-1

    while start <= end:
        mid = (start + end) // 2

        if A[mid] < num:
            start = mid + 1
        elif A[mid] > num:
            end = mid -  1
        else:
            return 1
    return 0


n = int(input())
A = list(map(int, input().split()))
m = int(input())
nums = list(map(int, input().split()))

A.sort()

for num in nums:
    print(binary_search(num, A))