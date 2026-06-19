def factorial(number: int) -> int:
    res = 1
    if number > 2:
        for i in range(2, number + 1):
            res *= i
        return res
    elif number > 0:
        return number
    else:
        print("cant do to - values.")



def main():
    print(factorial(-1))

if __name__ == '__main__':
    main()