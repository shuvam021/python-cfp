def binary_search(str_list: list, search_phrase: str) -> int:
    """
    Binary Search(toward <-)

    1. lo = 0, hi = len of iterable, find mid* value
    loop start
    2. iterable[middle] < search phrase; increment 'lo'
    3. else hi = middle
    loop end
    4. return lo
    """
    lo = 0
    hi = len(str_list)
    while lo < hi:
        mid = (lo + hi) // 2
        if str_list[mid] < search_phrase:
            lo = mid + 1
        else:
            hi = mid
    return lo


def insertion_sort(str_list: list):
    """
    Insertion Sort(Swap consecutive value)

    1. start with 1st position
    2. compare current element with prev element
    3. swap in asc or dsc
    4. increment position value
    """
    for i in range(1, len(str_list)):
        j = i - 1
        current_ele = str_list[i]
        prev_ele = str_list[j]
        while j >= 0 and current_ele < prev_ele:
            str_list[j + 1] = prev_ele
            j -= 1

        str_list[j + 1] = current_ele


def bubble_sort(list_ele: list) -> None:
    """
            [(64, 34), 25, 12, 22, 11, 90]
    1st     [34, 64, 25, 12, 22, 11, 90]
    2nd     [(34, 64, 25), 12, 22, 11, 90]
    2nd.1   [(34, 25, 64), 12, 22, 11, 90]
    2nd.2   [(25, 34, 64), 12, 22, 11, 90]
    3rd     [(25, 34, 64, 12), 22, 11, 90]  -> [12, 25, 34, 64, 22, 11, 90]
    4th     [(12, 25, 34, 64, 22), 11, 90]  -> [12, 22, 25, 34, 64, 11, 90]
    5th     [(12, 22, 25, 34, 64, 11,) 90]  -> [11, 12, 22, 25, 34, 64, 90]
    6th     [(11, 12, 22, 25, 34, 64, 90)]  -> [11, 12, 22, 25, 34, 64, 90]
    result = [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(list_ele)
    for i in range(n):
        i = 34
        for j in range(0, n - i - 1):
            j == list_ele[0]
            if list_ele[j] > list_ele[j + 1]:
                list_ele[j], list_ele[j + 1] = list_ele[j + 1], list_ele[j]


def merge_sort(str_list):
    if len(str_list) > 1:
        mid = len(str_list) // 2

        left = str_list[:mid]
        right = str_list[mid:]

        merge_sort(left)
        merge_sort(right)

        left_index = right_index = k = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                str_list[k] = left[left_index]
                left_index += 1
            else:
                str_list[k] = right[right_index]
                right_index += 1
            k += 1

        # Checking if any element was left
        while left_index < len(left):
            str_list[k] = left[left_index]
            left_index += 1
            k += 1

        while right_index < len(right):
            str_list[k] = right[right_index]
            right_index += 1
            k += 1


def binary_search_second(ele_list: list, search_ele: int):
    lo = 0
    hi = len(ele_list) - 1
    while lo <= hi:
        mid = lo + (hi-lo) // 2
        if search_ele == ele_list[mid]:
            return mid
        if ele_list[mid] < search_ele:
            lo = mid + 1
        if ele_list[mid] > search_ele:
            hi = mid - 1
    return -1
