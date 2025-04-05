import sys
input = sys.stdin.readline

def insertion_sort_count(A):
    count = 0
    for i in range(1, len(A)):
        for j in range(i-1, -1, -1):
            if A[i] < A[j]:
                if j == 0:
                    count += i
                    temp = A[i]
                    del A[i]
                    A.insert(0, temp)
                continue
            if A[i] > A[j]:
                count += i-j-1
                temp = A[i]
                del A[i]
                A.insert(j+1, temp)
                break
    return count



p = int(input())
for _ in range(p):
    temp = list(map(int, input().split()))
    case = temp[0]
    students = temp[1:]
    print(case, insertion_sort_count(students))
    

