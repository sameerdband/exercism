def square(number: int)->int:
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total()->int:
    grains: int = 0
    for index in range(1, 65):
        grains += square(index)
    return grains
