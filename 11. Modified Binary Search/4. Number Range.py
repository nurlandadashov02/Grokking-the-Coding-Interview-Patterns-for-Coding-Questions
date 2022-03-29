arr = [1, 3, 8, 10, 15]
key = 12


def binary_search(arr, key, findMaxIndex):
    keyIndex = -1
    low, high, mid = 0, len(arr) - 1, 0

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < key:
            low = mid + 1
        elif arr[mid] > key:
            high = mid - 1
        else:
            keyIndex = mid
            if findMaxIndex:
                low = mid + 1
            else:
                high = mid - 1

    return keyIndex


def number_range(arr, key):
    result = [-1, -1]
    result[0] = binary_search(arr, key, False)
    result[1] = binary_search(arr, key, True)
    return result


print(number_range(arr, key))
