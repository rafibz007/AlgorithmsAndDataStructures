
def insertion_sort(array : list) -> list:
    """
    Sorts array in place and additionally returns it.

    Algorithm iterates over all position in array and for every position sorts array from beginning
    to that position, by taking every new value, and transporting it towards beginning until
    left part of array is sorted.

    Stable: True

    Complexity: O(n^2)

    :param array: list of comparable elements
    :return: ascending sorted list
    """

    n = len(array)
    for i in range(1,n):
        j = i
        value = array[j]
        while j-1 >= 0 and array[j-1] > value:
            array[j] = array[j-1]
            j -= 1

        array[j] = value

    return array


# print(insertion_sort([-12, 235, 457, 23, 0, 12, 0, -10, 1]))
