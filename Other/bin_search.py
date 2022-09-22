def bin_search(array:list, value:int) -> int:
    """
    Sorts array in place and additionally returns it.

    Finds index of given value in sorted array, by recursively dividing
    searching area by half. Algorithm compares gives value with median of interval, if value is smaller,
    then look on the right, if bigger, then on the left, shrinking searched interval each time.

    Complexity: O(logn)

    :param value: value to look for
    :param array: list of sorted numbers
    :return: index of given value
    """

    left = 0
    right = len(array)-1

    while left <= right:
        mid = (left + right) // 2
        if array[mid] < value:
            left = mid+1
        elif array[mid] > value:
            right = mid-1
        else:
            return mid

    return -1


# print(bin_search([i for i in range(10)], 0))
# print(bin_search([i for i in range(10)], 9))
# print(bin_search([i for i in range(10)], 5))