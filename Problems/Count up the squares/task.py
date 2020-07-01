
add = 0
squared_sum = 0
while True:
    num = int(input())
    add += num
    squared_sum += num ** 2
    if add == 0:
        print(squared_sum)
        break