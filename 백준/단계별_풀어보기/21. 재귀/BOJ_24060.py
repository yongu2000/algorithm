def merge_sort(A, start, end, save):
    if start < end:
        mid = (start + end) // 2
        merge_sort(A, start, mid, save)
        merge_sort(A, mid + 1, end, save)
        merge(A, start, mid, end, save)

def merge(A, start, mid, end, save):
    tmp = []
    i = start
    j = mid + 1
    t = 0
    while (i <= mid and j <= end):
        if A[i] <= A[j]:
            tmp.append(A[i])
            save.append(A[i])
            i += 1
        else: 
            tmp.append(A[j])
            save.append(A[j])
            j += 1
    while (i <= mid):
        tmp.append(A[i])
        save.append(A[i])
        i += 1
    while (j <= end):
        tmp.append(A[j])
        save.append(A[j])
        j += 1
    i = start
    t = 0
    while (i <= end):
        A[i] = tmp[t]
        t += 1
        i += 1

n, k = map(int, input().split())
A = list(map(int, input().split()))
save = []
merge_sort(A, 0, len(A)-1, save)
print(save[k-1] if len(save) >= k else -1)