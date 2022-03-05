from random import randint

"""Day 06 Assignments"""


def fibonacci_series_program() -> list:
    series = [0, 1]
    limit = int(input("insert max length of fibonacci series: ")) - 2
    for i in range(limit):
        series.append(series[-1] + series[-2])
    print(series)
    return series


def perfect_number_program() -> None:
    num = int(input("Insert a number for perfect number check: "))
    series = [i for i in range(1, num) if num % i == 0]
    print(series)
    print(num, " is a perfect number" if num == sum(
        series) else " is not a perfect number")


def prime_number_program() -> None:
    num = int(input("Insert a number for prime number check: "))
    if num < 1:
        raise ValueError("Error: number can't be 0 or negative")
    series = [i for i in range(1, num + 1) if num % i == 0]
    print(num, " is Prime number" if series == [1, num] else " not a Prime no")


def reverse_number_program() -> None:
    reverse_number = 0
    temp = num = int(input("Insert a number to generate it's reverse: "))
    while temp > 0:
        remainder = temp % 10
        reverse_number = (reverse_number * 10) + remainder
        temp //= 10
    print(f"{reverse_number} is reverse of {num}")


def coupon_numbers_program() -> None:
    minimum = int(input("insert min range: "))
    maximum = int(input("insert max range: "))
    list_len = int(input("Insert a number of coupons to generate: "))
    if list_len > maximum - minimum:  # 200 # 210 # 20
        raise ValueError(
            f"no. of coupons {list_len} is less than range {maximum}-{minimum}")

    counter = 0
    coupons_list = []
    for i in range(list_len):
        counter += 1
        value = randint(minimum, maximum)
        if value not in coupons_list:
            coupons_list.append(value)

    print(f"Counter is {counter}")
    print(coupons_list)


if __name__ == '__main__':
    """Logical Programs"""
    # fibonacci_series_program()                            # Q 1
    # perfect_number_program()                              # Q 2
    # prime_number_program()                                # Q 3
    # reverse_number_program()                              # Q 4
    # coupon_numbers_program()                              # Q 5
