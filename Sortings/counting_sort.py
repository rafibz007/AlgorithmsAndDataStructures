def counting_sort(array:list) -> list:
    """
    Sorts array in place and additionally returns it.

    Counting sort is an algorithm for sorting a collection of objects according to keys that are
    small positive integers. It operates by counting the number of objects that possess distinct key values,
    and applying prefix sum on those counts to determine the positions of each key value in the output sequence.
    Its running time is linear in the number of items and the difference between the maximum key value and the
    minimum key value, so it is only suitable for direct use in situations where the variation in keys is
    not significantly greater than the number of items.

    Stable: True

    Complexity: O(n)

    :param array: list of small positive integers
    :return: ascending sorted list
    """

    max_index = max(array)+1
    array_len = len(array)
    buff_array = [0]*array_len
    counter = [0]*max_index

    for i in range(array_len):
        counter[array[i]] += 1
    for i in range(1,max_index):
        counter[i] += counter[i-1]

    for i in range(array_len-1, -1, -1):
        counter[array[i]] -= 1
        buff_array[counter[array[i]]] = array[i]

    for i in range(array_len):
        array[i] = buff_array[i]

    return array


# print(counting_sort([13, 235, 457, 23, 0, 12, 0, 12, 1]))
# print(counting_sort([0,0,0,1,0,0,0,2,0,0,0]))