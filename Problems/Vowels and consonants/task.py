a = input().strip()

for i in a:
    if i in "aeiou":
        print("vowel")
    # elif i in "!@#$%^&*()_+~{}:;'|/?.>,<":
    #     break
    elif i in 'bcdfghjklmnpqrstvwxyz':
        print("consonant")
    else:
        break