arr = [2, 4, 1, 4, 4]

i = 0
while i < len(arr):
    if arr[i] != i + 1:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            print(arr[i])
            break
    else:
        i += 1
