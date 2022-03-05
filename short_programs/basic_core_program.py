from random import randint

"""Day 05 Assignments"""


def flip_coin_program() -> None:
    tail_count = 0
    head_count = 0
    num_of_times = int(input("No of times you want to flip coin: "))
    for i in range(num_of_times):
        if randint(0, 10) < 5:
            tail_count += 1
        else:
            head_count += 1
    print("Total tail count is ", tail_count, " out of ", num_of_times)
    print("Total head count is ", head_count, " out of ", num_of_times)
    print("Total head ", float(head_count * 100) / num_of_times, "%")
    print("Total tail ", float(tail_count * 100) / num_of_times, "%")


def leap_year_program() -> None:
    year = int(input("Insert a Year to check leap-year: "))
    if year < 1000:
        raise Exception("Insert a valid year like 2022")
    print(year, "is leap year" if year % 400 == 0 and year %
          4 == 0 and year % 100 != 0 else "is not leap year")


def power_of_two_program() -> None:
    n = int(input("Insert a number: "))
    if 0 <= n < 31:
        for i in range(n + 1):
            print(f"2^{i} = {2 ** i}")
    else:
        print("Error: Out of range")


def harmonic_number_program() -> None:
    n = int(input("Insert a number for harmonic value = "))
    harmonic_value = 0
    if n != 0:
        for i in range(n + 1):
            harmonic_value += 1 / i
        print("Result: Harmonic of ", n, " is = ", harmonic_value)
    else:
        print("Error: value must be greater than 0")


def prime_factors_program() -> None:
    num = int(input("Please enter an integer for prime factorial = "))
    fact_list = []
    i = 2
    while num > 1:
        if num % i == 0:
            while num % i == 0:
                num /= i
            fact_list.append(i)
        i += 1
    print(fact_list)


def quotient_and_remainder_program() -> None:
    a = int(input("Enter 1st integer = "))
    b = int(input("Enter 2nd integer = "))
    print(f"Quotient: {a} / {b} = {a / b}")
    print(f"Remainder: {a} % {b} = {a % b}")


def swap_two_numbers_program() -> None:
    a = int(input("insert number a = "))
    b = int(input("insert number b = "))
    print(f"Pre Swap: a = {a}, and b = {b}")
    a, b = b, a
    print(f"Post Swap: a = {a}, and b = {b}")


def check_even_or_odd_program() -> None:
    num = int(input("insert number num = "))
    print(num, " is Even" if num % 2 == 0 else " is Odd")


def check_alphabet_is_vowels_program() -> None:
    val = input("insert an alphabet: ")
    if val is not None and val in ['a', 'e', 'i', 'o', 'u']:
        print(f"{val} is a Vowel")
    else:
        print(f"{val} is consonant")


def find_largest_number_program() -> None:
    arr = []
    maximum = 0
    a = int(input("range start: "))
    b = int(input("range end: "))
    list_length = int(input("insert length of array : "))
    for i in range(list_length):
        arr.append(randint(a, b))
    for i in arr:
        if maximum <= i:
            maximum = i
    print("===================================")
    print(arr)
    print(f"max value is: {maximum}")


if __name__ == "__main__":
    """Basic Core Programs"""
    # basic_core_program.flip_coin_program()                                   # Q 1
    # basic_core_program.leap_year_program()                                   # Q 2
    # basic_core_program.power_of_two_program()                                # Q 3
    # basic_core_program.harmonic_number_program()                             # Q 4
    # basic_core_program.prime_factors_program()                               # Q 5
    # basic_core_program.quotient_and_remainder_program()                      # Q 6
    # basic_core_program.swap_two_numbers_program()                            # Q 7
    # basic_core_program.check_even_or_odd_program()                           # Q 8
    # basic_core_program.check_alphabet_is_vowels_program()                    # Q 9
    # basic_core_program.find_largest_number_program()                         # Q 10
