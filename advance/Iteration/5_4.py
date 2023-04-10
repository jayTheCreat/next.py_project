import functools


def even_mul(num, index):
    """multple by 2 the numbers in a even index.
    :param num: the number to multiple
    :param index: the index 
    :type num: int
    :type index: int
    :return: the number after the multiple
    :rtype: int"""
    if index % 2 == 0:
        return num * 2
    return num


def num_to_digit_lst(num):
    """Turn a number to a list of his digits.
    :param num: the number to turn
    :type num: int
    :return: list of digits 
    :rtype: list"""
    return [int(x) for x in str(num)]


def check_id_valid(id_number):
    """Check if the id number given is valid (by the question definition).
    :param id_number: id number
    :type id_number: int
    :return: True if the number valid, False otherwise 
    :rtype: bool"""
    digits_lst = num_to_digit_lst(id_number)
    return (functools.reduce(lambda x, y: x + y,
                             map(lambda x: x if x < 10 else sum(num_to_digit_lst(x)),
                                 [even_mul(digits_lst[i], i + 1) for i in range(len(digits_lst))]))) % 10 == 0


MAX_NUMBER = 999999999


class IDIterator:
    """
    A class used to represent an ID Iterator
    """

    def __init__(self, id_num):
        """initialize the attribute in the class.
        :param id_num: id number for initializition
        :type id_num: int
        :return: none"""
        self._id = id_num  # 0 - 999999999

    def __iter__(self):
        """Returns the iterator instance.
        :return: iterator instance"""
        return self

    def __next__(self):
        """Returns the next valid id .
        :return: next valid id
        :rtype: int
        :raise: StopIteration"""
        while self._id <= MAX_NUMBER:
            self._id += 1
            if check_id_valid(self._id):
                return self._id
        raise StopIteration


def id_generator(id_num):
    """Generate the next valid id number.
    :param id_num: the id number
    :type id_num: int
    :return: next valid id number
    :rtype: int"""
    while id_num <= MAX_NUMBER:
        id_num += 1
        if check_id_valid(id_num):
            yield id_num


def main():
    id_number = int(input('Enter ID: '))
    choice = input('Generator or Iterator? (gen/it)? ')
    if choice == 'it':
        id_iter = IDIterator(id_number)
        for i in range(10):
            print(next(id_iter))
    elif choice == 'gen':
        id_gen = id_generator(id_number)
        for i in range(10):
            print(next(id_gen))


if __name__ == "__main__":
    main()
