import string


class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, char, index):
        self._char = char
        self._index = index

    def __str__(self):
        return f'The username contains an illegal character "{self._char}" at index {self._index}'


class UsernameTooShort(Exception):
    def __str__(self):
        return "The username is too short"


class UsernameTooLong(Exception):
    def __str__(self):
        return "The username is too long"


class PasswordMissingCharacter(Exception):
    def __init__(self):
        pass

    def __str__(self):
        return "The password is missing a character"


class PasswordMissingUppercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Uppercase)'


class PasswordMissingLowercase(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Lowercase)'


class PasswordMissingDigit(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Digit)'


class PasswordMissingSpecial(PasswordMissingCharacter):
    def __str__(self):
        return super().__str__() + ' (Special)'


class PasswordTooShort(Exception):
    def __str__(self):
        return "The password is too short"


class PasswordTooLong(Exception):
    def __str__(self):
        return "The password is too long"


def check_input(username, password):
    pw_validator = {"Lower": 0, "Upper": 0, "Digit": 0, "Special": 0}
    try:
        if len(username) < 3:
            raise UsernameTooShort
        if len(username) > 16:
            raise UsernameTooLong
        if len(password) < 8:
            raise PasswordTooShort
        if len(password) > 40:
            raise PasswordTooLong

        for i in range(len(username)):
            if username[i] not in string.ascii_letters + string.digits + '_':
                raise UsernameContainsIllegalCharacter(username[i], i)

        for x in password:
            if x in string.ascii_lowercase:
                pw_validator["Lower"] += 1
            elif x in string.ascii_uppercase:
                pw_validator["Upper"] += 1
            elif x in string.digits:
                pw_validator["Digit"] += 1
            elif x in string.punctuation:
                pw_validator["Special"] += 1

        if pw_validator["Lower"] == 0:
            raise PasswordMissingLowercase
        elif pw_validator["Upper"] == 0:
            raise PasswordMissingUppercase
        elif pw_validator["Digit"] == 0:
            raise PasswordMissingDigit
        elif pw_validator["Special"] == 0:
            raise PasswordMissingSpecial

    except UsernameTooShort as e:
        print(e)
    except UsernameTooLong as e:
        print(e)
    except PasswordTooShort as e:
        print(e)
    except PasswordTooLong as e:
        print(e)
    except UsernameContainsIllegalCharacter as e:
        print(e)
    except PasswordMissingCharacter as e:
        print(e)

    else:
        print("OK")


def main():
    check_input("1", "2")
    check_input("0123456789ABCDEFG", "2")
    check_input("A_a1.", "12345678")
    check_input("A_1", "2")
    check_input("A_1", "ThisIsAQuiteLongPasswordAndHonestlyUnnecessary")
    check_input("A_1", "abcdefghijklmnop")
    check_input("A_1", "ABCDEFGHIJLKMNOP")
    check_input("A_1", "ABCDEFGhijklmnop")
    check_input("A_1", "4BCD3F6h1jk1mn0p")
    check_input("A_1", "4BCD3F6.1jk1mn0p")


if __name__ == '__main__':
    main()
