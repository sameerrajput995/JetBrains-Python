def tax_percent(income):
    if income <= 15527:
        tax = 0
        # print(f'The tax for {income} is {tax}%. That is {income * tax / 100} dollars!')
    elif 15528 <= income <= 42707:
        tax = 15
        # print(f'The tax for {income} is {tax}%. That is {income * tax / 100} dollars!')
    elif 42708 <= income <= 132406:
        tax = 25
    else:
        tax = 28
    return f'The tax for {income} is {tax}%. That is {round(income * tax / 100)} dollars!'


print(tax_percent(int(input())))
