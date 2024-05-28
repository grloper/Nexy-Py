def four_dividers(number):
    return list(filter(lambda x: x % 4 == 0, range(1, number+1)))