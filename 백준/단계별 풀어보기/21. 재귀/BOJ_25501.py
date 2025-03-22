def recursion(s, l, r, c):
    if l >= r : 
        return 1, c
    elif s[l] != s[r]: 
        return 0, c
    return recursion(s, l+1, r-1, c+1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

t = int(input())

for _ in range(t):
    s = input()
    ret, count = isPalindrome(s)
    print(ret, count)