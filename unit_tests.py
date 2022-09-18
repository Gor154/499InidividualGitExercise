import main_code


def test_if_even():
    number = 25
    assert main_code.is_even(number) is False


def test_if_prime():
    number = 59
    assert main_code.is_prime(number) is True
    number = 222
    assert main_code.is_prime(number) is False

def test_output(capfd):
    number = 345
    main_code.break_up(number)
    out, err = capfd.readouterr()
    assert(out) == "Hundreds: 3 Tens: 4 Ones: 5\n345 is odd\n"