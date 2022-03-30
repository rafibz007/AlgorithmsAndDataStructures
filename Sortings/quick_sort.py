from typing import Tuple


def quick_sort(array: list) -> list:
    """
    Sorts array in place and additionally returns it.

    Recursively divides and sorts parts of an array. On every sort call on part of an array,
    algorithm picks among its values one - which ideally would be median - and sets it as pivot, then
    organise array putting all elements less than pivot on the left, equal in the middle and rest on
    the right in unorganised way.
    After reorganisation algorithm recursively sort each part the same way, treating part of length one as sorted.

    Pivots after reorganisation has all smaller elements on the left, and larger on the right, then they are already
    on the position they would be, if the whole array would be sorted.

    Stable: False

    Complexity: O(nlogn)

    :param array: list of comparable elements
    :return: ascending sorted list
    """

    def sort(start: int, end: int):
        """
        Call partition in order to reorganise part of array, and recursively sort each of received new parts.
        """
        nonlocal array

        if start < end:
            pivot_start, pivot_end = partition(start, end)
            sort(start, pivot_start - 1)
            sort(pivot_end + 1, end)

    def partition(start: int, end: int) -> Tuple[int, int]:
        """
        Picks pivot by taking first number of this part of array and reorganise this section of array, returning
        index on which pivot ended. Magic fives algorithm can be used to find better pivot.

        Pivots stay at ending position, and gets swapped at the end of partition.

        Partitioning works as follows: algorithm iterates over part of an array and keeps index of less
        section. Each time it finds value that should be in this section it swaps values extending it and updates
        section pointer. If value equal to pivot had been found, then it gets swapped to the end and amount
        of found pivots gets updated.

        :returns: pivots_section_start, pivots_section_end
        """
        nonlocal array

        pivot = array[start]
        array[start], array[end] = array[end], array[start]

        pivots_amount = 1
        section_index = start - 1

        i = start
        while i < end-pivots_amount+1:
            if array[i] < pivot:
                section_index += 1
                array[i], array[section_index] = array[section_index], array[i]
            if array[i] == pivot:
                array[end-pivots_amount], array[i] = array[i], array[end-pivots_amount]
                pivots_amount += 1

                # in order to check swapped value again
                i -= 1

            i += 1

        section_index += 1
        for i in range(pivots_amount):
            array[section_index+i], array[end-i] = array[end-i], array[section_index+i]

        return section_index, section_index+pivots_amount-1

    n = len(array)
    sort(0, n-1)
    return array


print(quick_sort([-12, 235, 457, 23, 0, 12, 0, -10, 1]))
