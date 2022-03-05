"""Programs for NUnit Testing"""


def vending_machine_program(cash_input: int) -> bool:
    temp = cash_input

    available_cash = [1000, 500, 100, 50, 10, 5, 2, 1]
    after_changes = {}
    for c in available_cash:
        if temp >= c:
            no_of_notes = temp // c
            temp %= c
            after_changes.update({c: no_of_notes})
        if temp == 0:
            break
    if cash_input != sum([k * v for k, v in after_changes.items()]):
        return False
    print(after_changes)
    return True


def day_of_week(d: int = None, m: int = None, y: int = None) -> str:
    if d == m == y is None:
        d = int(input("Insert Date: "))
        m = int(input("Insert Month: "))
        y = int(input("Insert Year: "))
    y0 = y - ((14 - m) // 12)
    x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
    m0 = (m + (12 * ((14 - m) // 12)) - 2)
    d0 = (d + x + ((31 * m0) // 12)) % 7

    options = {0: "Sunday", 1: "Monday", 2: "Tuesday",
               3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday"}
    return f"Day is : {options[d0]}"


def temperature_conversion(temp: float = None, temp_type: str = None) -> float:
    if temp == temp_type is None:
        temp = float(input("insert temperature = "))
        temp_type = input("insert scale C/F: ")
    result = 0
    if temp_type.lower() == 'c':
        result = (temp - 32) * 0.56
    if temp_type.lower() == 'f':
        result = (temp * 1.8) + 32
    print('result: ', result)
    return result


def monthly_payment() -> float:
    principal = float(input("Enter Principal loan amount = "))
    year = int(input("Enter years to pay = "))
    rate = int(input("Enter rate of interest = "))
    n = 12 * year
    r = (rate / (12 * 100))
    payment = (principal * r) / (1 - (1 + r) ** (-1 * n))
    print(f"you have to pay {payment}/m")
    return payment


if __name__ == '__main__':
    """Programs for NUnit Testing"""
    vending_machine_program(int(input("Insert your cash amount: ")))    # Q 1
    day_of_week()                                                       # Q 2
    temperature_conversion()                                            # Q 3
    monthly_payment()                                                   # Q 4
    # TODO: N-unit test - Q 5,
    # TODO: N-unit test - Number to Binary conversion(6),
    # TODO: N-unit test - nibble_to_binary(7)
