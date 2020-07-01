def deposit(amount):
    year = 0
    while amount < 700000:
        interest = (0.071 * amount)
        amount += interest
        year += 1
    return year


print(deposit(int(input())))