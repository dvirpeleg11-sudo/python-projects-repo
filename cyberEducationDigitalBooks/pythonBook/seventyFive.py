def factorial(number: int) -> int:
    res = 1
    if number > 2:
        for i in range(number, 2, -1):
            res *= i