def is_sorted(arr):

    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[j] < arr[i]:
                return False
    return True


print(is_sorted([1, 5, 10, 15]))


def is_sorted_efficient(arr):

    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            return False
    return True


print(is_sorted_efficient([1]))
