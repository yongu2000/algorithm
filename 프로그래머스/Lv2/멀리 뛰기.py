# https://school.programmers.co.kr/learn/courses/30/lessons/12981

def solution(n, words):
    answer = [0, 0]

    prev = ''
    used = set()
    for idx, word in enumerate(words):
        player = (idx % n) + 1
        turn = (idx // n) + 1
        if (prev != '' and word[0] != prev[-1]) or word in used:
            answer = [player, turn]
            break
        prev = word
        used.add(word)

    return answer

print(solution(3, 	["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"])) # 5
print(solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang", "gather", "refer", "reference", "estimate", "executive"])) # 3
print(solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])) # 3




