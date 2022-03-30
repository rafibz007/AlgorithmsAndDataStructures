
def selection_sort(array : list) -> list:
    """
    Sorts array in place and additionally returns it.

    Algorithm iterates over all position in array and for every position finds next minimal value
    that should be in this place and swap places with value on current position. On every iteration
    on the left of current position values are sorted in ascending order, whereas on the right
    algorithm looks for next value, among unsorted larger values.

    Stable: True

    Complexity: O(n^2)

    :param array: list of comparable elements
    :return: ascending sorted list
    """

    n = len(array)
    for i in range(n):

        min_value = float("Inf")
        min_index = i
        for j in range(i,n):
            if array[j] < min_value:
                min_index = j
                min_value = array[min_index]

        array[i], array[min_index] = array[min_index], array[i]

    return array


# print(selection_sort([-12, 235, 457, 23, 0, 12, 0, -10]))