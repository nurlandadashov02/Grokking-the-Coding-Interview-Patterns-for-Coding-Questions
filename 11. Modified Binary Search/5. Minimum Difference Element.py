arr = [4, 6, 10]
key = 7

def min_diff(arr, target):
    low, mid, high = 0, 0, len(arr) - 1

    while low <= high:
        mid = (high + low) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1
        else:
            return arr[mid]

    if (arr[low] - target) < (key - arr[high]):
        return arr[low]

    return arr[high]

print(min_diff(arr, key))
