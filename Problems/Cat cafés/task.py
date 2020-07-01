def cat_cafe():
    cafe_list = []
    while True:
        cafe = input().strip()
        if cafe != "MEOW":
            cafe_list.append(cafe)
        else:
            break
    num = [int(cafe_list[i].split(" ")[1]) for i in range(len(cafe_list))]
    return cafe_list[num.index(max(num))].split(" ")[0]


print(cat_cafe())
