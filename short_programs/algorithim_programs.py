from utils.helper_methods import primes
from utils.search_algo import (binary_search, binary_search_second,
                               bubble_sort, insertion_sort, merge_sort)
import math

"""Algorithm Programs"""


def string_permutation(string, probability: str = '', combination: list = []) -> list:
    """question no 01 """
    if len(string) == 0:
        combination.append(probability)
        return

    for i in range(len(string)):
        string_permutation(string[0:i] + string[i + 1:],
                           probability + string[i], combination)
    return combination


def binary_search_the_word_from_word_list():
    """question no 02 """
    str_list = ["contribute", "geeks", "ide", "practice"]
    phrase = "practice"
    result = binary_search(str_list, phrase)
    if str_list[result] != phrase:
        print("Element not present")
    else:
        print(f"Element is list[{result}] =", str_list[result])


def insertion_sort_implementation():
    """question no 03 """
    str_list = ['za', 'nk', 'ab', 'ja', 'ia']
    print("Insertion Sort: ")
    print("Given list is: \n", str_list)
    insertion_sort(str_list)
    print("Sorted list is: \n", str_list)


def bubble_sort_implementation():
    """question no 04"""
    print("Bubble Sort: ")
    str_list = [64, 34, 25, 12, 22, 11, 90]
    print("Given list is: \n", str_list)
    bubble_sort(str_list)
    print("Sorted list is: \n", str_list)


def merge_sort_implementation():
    """question no 05"""
    str_list = [12, 11, 13, 5, 6, 7]
    print("Given list is: \n", str_list)
    merge_sort(str_list)
    print("Sorted list is: \n", str_list)


def anagram_detection(str1, str2):
    """question no 06"""
    list1 = list(str1)
    list2 = list(str2)
    list1.sort()
    list2.sort()
    if len(list1) == len(list2):
        return True if list1 == list2 else False
    return False


def get_prime_nos(x: int = 0, y: int = None) -> list:
    """question no 07"""
    if not y:
        y = int(input("insert max range to get prime nos: "))
    return primes(x, y)


def get_prime_palindrome(x):
    """question no 08"""
    prime_palindrome = []
    for num in primes(x):
        temp = num
        rev = 0
        while temp > 0:
            dig = temp % 10
            rev = rev * 10 + dig
            temp = temp // 10
        if num == rev:
            prime_palindrome.append(num)
    return prime_palindrome


def guess_a_number():
    """question no 10"""
    N = int(input("range: "))
    n = int(math.log(N, 2))
    num_list = [i for i in range(N)]
    print(num_list)
    user_input = int(input(f"guess a number from 0 - {n}: "))
    position = binary_search_second(ele_list=num_list, search_ele=user_input)
    print("not found" if position == -1 else f"found at  = {position} position")


def string_replace_program(msg: str = "", val: dict = {}):
    """question no 12"""
    message = """
    Read in the following message: Hello <<name>>, We have your full name as <<full name>> in our system.
    your contact number is 91-xxxxxxxxxx.
    Please,let us know in case of any clarification Thank you BridgeLabz XX/XX/XXXX, 91-xxxxxxxxxx.
    """
    value_dict = {
        "<<name>>": "Shuvam",
        "<<full name>>": "Shuvam Das",
        "91-xxxxxxxxxx": "91-9123654780",
        "XX/XX/XXXX": "01/01/2016"
    }

    if msg == "" and len(val) == 0:
        msg, val = message, value_dict

    for k, v in val.items():
        if k in msg:
            msg = msg.replace(k, v)
    print(msg)
    return msg


if __name__ == '__main__':
    """Algorithm Programs"""
    # print(string_permutation(string='val'))                 # Q 1
    # binary_search_the_word_from_word_list()                 # Q 2
    # insertion_sort_implementation()                         # Q 3
    # bubble_sort_implementation()                            # Q 4
    # merge_sort_implementation()                             # Q 5
    # print(anagram_detection('heart', 'earth'))              # Q 6
    # #
    # print(get_prime_nos())                                  # Q 7
    # print(get_prime_palindrome(1001))                       # Q 8
    # TODO: Q. 9 (Algorithm Programs)
    # guess_a_number()                                        # Q 10
    # TODO: Q. 11 (Algorithm Programs)
    # string_replace_program()                                # Q 12
