
add = 0
count = 0
while True:
    num = input()
    if num == '.':
        break
    else:
        add += int(num)
        count += 1
print(add / count)