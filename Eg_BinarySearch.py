def binary_search(array, target):
    lower = 0
    upper = len(array) - 1   # last index

    while lower <= upper:
        mid = lower + (upper - lower) // 2
        val = array[mid]

        if target == val:
            return mid
        elif target > val:
            lower = mid + 1
        else:
            upper = mid - 1

    return -1   # not found


# Example usage
l = [1, 2, 3, 4, 5, 6, 7]
print(binary_search(l, 5))