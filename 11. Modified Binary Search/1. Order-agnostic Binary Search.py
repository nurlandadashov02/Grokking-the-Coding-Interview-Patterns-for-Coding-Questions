arr = [4, 6, 10]
key = 10

asc = arr[0] < arr[1]

low, high, mid = 0, len(arr) - 1, 0

while low <= high:
    mid = (high + low) // 2

    if arr[mid] < key:
        if asc:
            low = mid + 1
        else:
            high = mid - 1
    elif arr[mid] > key:
        if asc:
            low = mid + 1
        else:
            high = mid - 1
    else:
        break

print(mid)