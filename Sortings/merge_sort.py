
def merge_sort(array : list) -> list:
    """
    Sorts array in place and additionally returns it.

    Algorithm recursively divides array in half and join its sorted parts together.
    Recursive division will last until array of length one occures, so we can treat it
    as sorted.

    Joining sorted arrays relies on iterating both sorted halves and
    inserting to main array smallest unused value, which will always be on one of the beginnings of
    unused sorted sub array's values.

    Stable: True

    Complexity: O(nlogn)

    :param array: list of comparable elements
    :return: ascending sorted list
    """

    def merge(start:int, mid, end:int):
        """
        Merges sorted halves into one sorted array and save result in array.
        Uses buff_array to temporarily store values and enable sorting.
        """
        nonlocal array, buff_array

        for i in range(start, end+1):
            buff_array[i] = array[i]

        left_index = start
        right_index = mid+1

        left_end = mid+1
        right_end = end+1

        array_index = start
        while left_index < left_end and right_index < right_end:
            if buff_array[left_index] < buff_array[right_index]:
                array[array_index] = buff_array[left_index]
                left_index += 1
            else:
                array[array_index] = buff_array[right_index]
                right_index += 1
            array_index += 1

        # copy rest of one unused one of halves
        while left_index < left_end:
            array[array_index] = buff_array[left_index]
            left_index += 1
            array_index += 1

        while right_index < right_end:
            array[array_index] = buff_array[right_index]
            right_index += 1
            array_index += 1

    def sort(start:int, end:int):
        """
        Recursively calls itself on halves of array to sort them, and merge after that.
        Recursion ends on arrays of length one which we assume is sorted.
        """
        nonlocal array

        if start < end:
            mid = (start + end) // 2
            sort(start, mid)
            sort(mid+1, end)
            merge(start, mid, end)

    n = len(array)
    buff_array = [0]*n
    sort(0, n-1)
    return array


print(merge_sort([-12, 235, 457, 23, 0, 12, 0, -10, 1]))