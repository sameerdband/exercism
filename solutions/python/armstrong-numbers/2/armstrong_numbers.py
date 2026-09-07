def is_armstrong_number(number):
    digits: list[int] = [int(digit) for digit in str(number)]
    num_digits: int = len(digits)
    return sum(digit ** num_digits for digit in digits) == number