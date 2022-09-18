import math


def break_up(number: int):
    print("Hundreds: " + str(number // 100 % 10) + " Tens: " + str(number // 10 % 10) + " Ones: " + str(number % 10))
    is_even(number)


def is_even(number: int):
    if number % 2 == 0:
        print(str(number)+" is even")
        return True
    else:
        print(str(number) + " is odd")
        return False


def is_prime(number: int):
    for i in range(2, int(math.sqrt(number)) + 1):
        if (number % i) == 0:
            return False
    return True


def main():
    number = 0
    while int(number) < 1 or int(number) > 999:
        number = input("Enter an integer from 1 to 999: ")
        if not number.isnumeric():
            number = 0
    break_up(int(number))
    if is_prime(int(number)):
        print(number+" is prime")
    else:
        print(number+" is not prime")


if __name__ == "__main__":
    main()