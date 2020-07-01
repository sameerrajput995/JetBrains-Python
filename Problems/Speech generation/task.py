def text_to_speech(num):
    return ["zero" if i == '0' else "one" if i == '1' else "two" if i == "2"
            else "three" if i == "3" else "four" if i == "4" else "five" if i == "5"
            else "six" if i == "6" else "seven" if i == "7" else "eight" if i == "8"
            else "nine" for i in num]


print(*text_to_speech(input()), sep="\n")
