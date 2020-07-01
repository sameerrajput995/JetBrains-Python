
def half_life(initial, final):
    counter = 1
    while initial / 2 > final:
        counter += 1
        initial /= 2
    print(counter * 12)


half_life(int(input()), int(input()))
