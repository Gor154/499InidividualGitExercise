def break_up(number: int):
    print("Hundreds: " + str(number // 100 % 10) + " Tens: " + str(number // 10 % 10) + " Ones: " + str(number % 10))


def main():
    number = 0
    while int(number) < 1 or int(number) > 999:
        number = input("Enter a number from 1 to 999: ")
    break_up(int(number))


if __name__ == "__main__":
    main()