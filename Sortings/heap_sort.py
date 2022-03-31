def heap_sort(array: list) -> list:
    """
        Sorts array in place and additionally returns it.

        Algorithm builds a max heap from array, pops biggest values from it until heap is empty and puts
        them at the end of array.

        Heap - data structure, build of nodes containing values. All nodes have two children (left and right) and
        its value is greater than its children (so also than all nodes below it). Heap implemented as array.

        Pivots after reorganisation has all smaller elements on the left, and larger on the right, then they are already
        on the position they would be, if the whole array would be sorted.

        Stable: False

        Complexity: O(nlogn)

        :param array: list of comparable elements
        :return: ascending sorted list
        """

    array_len = len(array)

    def parent(i: int) -> int:
        """:returns: parent index"""
        return (i - 1) // 2

    def left(i: int) -> int:
        """:returns: left child index"""
        return 2 * i + 1

    def right(i: int) -> int:
        """:returns: right child index"""
        return 2 * i + 2

    def heapify(i: int, n: int):
        """
        Repairs heap from node i, down to bottom of the heap.
        Finds the biggest number among node and its two children and swaps values to maintain
        heap properties, by transporting the largest number to the top.

        If values where swapped, node i fulfils heap properties, because it has only smaller numbers
        in its left and right sub heaps. But sub heap from which value was taken can be invalid, so
        algorithm heapify it recursively.


        :param n: amount of heap nodes
        :param i: node index
        """
        nonlocal array

        max_i = i
        left_i = left(i)
        right_i = right(i)

        if left_i < n and array[max_i] < array[left_i]: max_i = left_i
        if right_i < n and array[max_i] < array[right_i]: max_i = right_i

        if max_i != i:
            array[i], array[max_i] = array[max_i], array[i]
            heapify(max_i, n)

    def pop(n:int) -> any:
        """
        Swaps heap max value, with one of the smallest nodes and repairs the heap by calling heapify and
        updating heap number of elements, so that swapped max value would not be considered a heap member anymore.

        :param n: amount of heap nodes
        :return: heap max value
        """
        nonlocal array

        array[n-1], array[0] = array[0], array[n-1]
        heapify(0, n-1)
        return array[n-1]

    def build_heap():
        """
        Build heap from array, by calling heapify from bottom nodes up to the top.
        This way the biggest values get transferred upward.
        """
        nonlocal array, array_len

        for i in range(parent(array_len-1), -1, -1):
            heapify(i,array_len)

    def sort():
        """
        Build heap out of array and by using pop gets the largest values and sorts them.
        """
        nonlocal array
        build_heap()
        for i in range(array_len-1, -1, -1):
            # array[i] = pop(i+1)
            # simply pop is enough, but that is only due to implementation of this function
            pop(i+1)

    sort()
    return array


# print(heap_sort([-12, 235, 457, 23, 0, 12, 0, -10, 1]))
# print(heap_sort([0,0,0,1,0,0,0,-1,0,0,0]))
