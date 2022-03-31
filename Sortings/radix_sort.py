from insertion_sort import insertion_sort

def radix_sort(array:list) -> list:
    """
    Sorts array in place and additionally returns it.

    Sorts array by stably sorting items relative to positions of its digits, starting
    from lest significant to most important position.

    For stable sorts relative to positions counting sort can be used,
    because most often each position has finite set of values, like
    digits in numbers 0..9, or letters a-zA-Z.

    Stable: True

    Complexity: O(nw) w - key length

    :param array: list of positive integers
    :return: ascending sorted list
    """

    def counting_sort(array: list, f = lambda x: x) -> list:
        """
        Sorts array in place and additionally returns it.

        Custom counting sort, that allows counting relative to particular position in array.

        :param f: function to get digit value from key for counting and sorting
        :param array: list of small integers
        :return: ascending sorted list
        """

        max_index = 9+1
        array_len = len(array)
        buff_array = [0] * array_len
        counter = [0] * max_index

        for i in range(array_len):
            counter[f(array[i])] += 1
        for i in range(1, max_index):
            counter[i] += counter[i - 1]

        for i in range(array_len - 1, -1, -1):
            counter[f(array[i])] -= 1
            buff_array[counter[f(array[i])]] = array[i]

        for i in range(array_len):
            array[i] = buff_array[i]

        return array

    def custom_f(index:int):
        return lambda x: x[index] if 0<=index<len(x) else 0

    # example implementation for integers
    array_len = len(array)

    # splits every number in array to array of its digits, it is not a good practice, and definitely
    # I could achieve same thing by using lambdas with modulo division and integer division,
    # but for code and example simplicity I've done it like this
    max_val = max(array)
    array = list(map(str, array))
    array = list(map(lambda x: list(map(int, x[::-1])), array))

    for i in range(len(str(max_val))):
        counting_sort(array, custom_f(i))

    # return default array values
    array = list(map(lambda x: int(''.join(map(str, x[::-1]))), array))
    return array


# print(radix_sort([235, 412312357, 23123, 0, 12, 0, 199]))
# print(radix_sort([0,1230,0,1,1230,20,1230, 2221,0,1231,1231230]))