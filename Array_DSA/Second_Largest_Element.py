def second_largest(arr):

    res = arr[0]
    largest = max(arr)
    arr.remove(largest)

    for values in arr:
        if res < values:
            res = values

    if res == largest:
        return -1
    return res


print(second_largest([1, 9, 6, 0, 8]))
