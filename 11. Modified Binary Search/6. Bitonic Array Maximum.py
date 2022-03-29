def max_val(arr):
    print(arr)
    low, mid, high = 0, 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if mid < len(arr) - 1 and arr[mid] < arr[mid + 1]:
            low = mid + 1
        elif mid > 1 and arr[mid] < arr[mid - 1]:
            high = mid - 1
        else:
            break

    print(low, mid, high)
    return arr[mid]

print(max_val([1, 3, 8, 12, 4, 2]))
print(max_val([3, 8, 3, 1]))
print(max_val([1, 3, 8, 12]))
print(max_val([10, 9, 8]))
