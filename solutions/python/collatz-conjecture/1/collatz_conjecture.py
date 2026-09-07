def steps(number: int):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    completed_steps: int = 0
    while (number != 1):
        number = number / 2 if number % 2 == 0 else number * 3 + 1
        completed_steps += 1
    return completed_steps
