def is_armstrong_number(number):
    digits: list[int] = [int(d) for d in str(number)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == number