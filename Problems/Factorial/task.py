def factorial(number):
    i = 2
    res = 2
    while i < number:
        res *= (i + 1)
        i += 1
    return res


print(factorial(int(input())))
