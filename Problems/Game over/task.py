scores = input().split()
# put your python code here
count_c = 0
count_i = 0

for i in scores:
    if i == "C":
        count_c += 1
    else:
        count_i += 1
        if count_i == 3:
            print("Game over")
            print(count_c)
            break
else:
    print("You won")
    print(count_c)
