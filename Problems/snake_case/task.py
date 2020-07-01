def snake_case(word):
    lst = []
    for i in word:
        if i.isupper():
            lst.append("_" + i.lower())
        else:
            lst.append(i)
    return "".join(lst).lstrip("_")


# def snake_case(word):
#     return "".join(["_" + i.lower() if i.isupper() else i for i in word]).lstrip("_")


print(snake_case(input().strip()))
