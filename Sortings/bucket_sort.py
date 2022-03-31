from insertion_sort import insertion_sort

def bucket_sort(array:list) -> list:
    """
    Sorts array in place and additionally returns it.

    Algorithm creates buckets and assign each item of array to one of them, depending on its value.
    Number of buckets is equal to amount of elements in array.
    Assuming that values in array comes from uniform distribution, in each of buckets we should have
    small number of elements. We can sort each bucket and join them to sort entire array.

    To sort buckets here I use insertion sort, but for example merge sort can be used,
    in order to ensure that maximum complexity would be O(nlogn) and not O(n^2) if values
    did not come from uniform distribution.

    Stable: True

    Complexity: O(n)

    :param array: list of numbers with values from uniform distribution
    :return: ascending sorted list
    """

    array_len = len(array)
    buckets = [ [] for _ in range(array_len) ]

    max_val = max(array)
    min_val = min(array)

    value_range = (max_val-min_val)/array_len

    for i in range(array_len):
        ratio = (array[i] - min_val) / value_range
        diff = ratio - int(ratio)

        if diff == 0 and array[i] != min_val:
            buckets[int(ratio) - 1].append(array[i])
        else:
            buckets[int(ratio)].append(array[i])

    array_index = 0
    for buck in buckets:
        insertion_sort(buck)
        for i in range(len(buck)):
            array[array_index] = buck[i]
            array_index += 1

    return array


# print(bucket_sort([-12, 235, 457, 23, 0, 12, 0, -10, 1]))
# print(bucket_sort([0,0,0,1,0,0,0,-1,0,0,0]))