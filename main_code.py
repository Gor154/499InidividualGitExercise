def break_up(number: int):
    print("Hundreds: " + str(number // 100 % 10) + " Tens: " + str(number // 10 % 10) + " Ones: " + str(number % 10))
    is_even(number)


def is_even(number: int):
    if number % 2 == 0:
        print(str(number)+" is even")
    else:
        print(str(number) + " is odd")


def main():
    number = 0
    while int(number) < 1 or int(number) > 999:
        number = input("Enter an integer from 1 to 999: ")
        if not number.isnumeric():
            number = 0
    break_up(int(number))


if __name__ == "__main__":
    main()