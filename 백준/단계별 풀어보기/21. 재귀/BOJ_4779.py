def cantor(init, n):
    if n == 0:
        return "-"
    sl = 3**(n-1)
    left = init[0:sl]
    mid = " "*sl
    right = init[sl*2:]

    return cantor(left, n-1) + mid + cantor(right, n-1)

while True:
    try:
        n = int(input())
    except:
        break

    init = "-"*3**n
    print(cantor(init, n))