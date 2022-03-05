def primes(x=0, y=1000):
    return [i for i in range(x, y) if 0 not in [i % j for j in range(2, i)]]


def anagram(data: list):
    """
    filter item and it's anagram from given list
    anagram: earth, heart are anagram.

    :param data: list possible anagram items
    :return: list of item and its anagram
    """
    return [i for i in data for j in data if i != j and sorted(str(i)) == sorted(str(j))]
