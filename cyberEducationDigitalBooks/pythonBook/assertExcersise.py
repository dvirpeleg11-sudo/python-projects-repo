NUMBER = 5
CHEZKA = 3
RESULT = 125


def power_func(number, chezka):
    result = 1
    for i in range(chezka):
        result *= number
    return result


def main():
    #     try:
    #         assert (power_func(NUMBER, CHEZKA)) == RESULT
    #         print("your assertion {} ^ {} = {} is true. well done!".format(NUMBER, CHEZKA, RESULT))
    #     except AssertionError:
    #         print("your assertion {} ^ {} = {} is false.".format(NUMBER, CHEZKA, RESULT))
    #     finally:
    #         print("the end.")
    assert (power_func(NUMBER, CHEZKA)) == RESULT, "your assertion {} ^ {} = {} is false.".format(NUMBER, CHEZKA,
                                                                                                  RESULT)
    print("your assertion {} ^ {} = {} is true. well done!".format(NUMBER, CHEZKA, RESULT))


if __name__ == "__main__":
    main()
