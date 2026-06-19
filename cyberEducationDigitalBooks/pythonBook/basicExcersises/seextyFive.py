def printNumDetiles(str_num: str):

    print(f"you entered the number {str_num}")
    digits = ""

    for str_digit in str_num:
        digits += str_digit + ", "

    print(f"the digits of this number are: {digits}")

    sum_digits = 0
    for str_digit in str_num:
        int_digit = int(str_digit)
        sum_digits += int_digit
    print(f"the some of digits is: {sum_digits}")

def main():
    str_num = input("please enter a 5 digits number: ")
    printNumDetiles(str_num)

if __name__ == "__main__":
    main()