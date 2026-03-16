def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        prev = phone_book[i-1]
        cur = phone_book[i]
        if cur[:len(prev)] == prev:
            return False
    return True