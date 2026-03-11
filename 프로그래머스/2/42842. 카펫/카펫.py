def solution(brown, yellow):
    height = 3
    while True:
        if yellow % (height - 2) == 0 and brown == 2 * height + 2 * (yellow // (height - 2)):
            return [(yellow // (height - 2))+2, height]
        height += 1
