import sys, re
input = sys.stdin.readline

def has_vowel(password):
    if not re.search(r"[aeiou]", password):
        return False
    return True

def no_three_vowel_or_consonant(password):
    if re.search(r"[aeiou]{3}", password) or re.search(r"[^aeiou]{3}", password):
        return False
    return True

def no_two_letters(password):
    if re.search(r"(.)\1", password):
        if not re.search(r"(ee|oo)", password):  
            return False
        for m in re.finditer(r"(.)\1", password):
            if m.group(0) not in ["ee", "oo"]:
                return False
    return True

while True:
    password = input().strip()
    if password == "end":
        break

    if has_vowel(password) and no_three_vowel_or_consonant(password) and no_two_letters(password):
        print(f"<{password}> is acceptable.")
    else:
        print(f"<{password}> is not acceptable.")