arr = [5, 4, 7, 2, 3, 5, 3]

i = 0
duplicates = []
while i < len(arr):
    if arr[i] != i + 1:
        j = arr[i] - 1
        if arr[i] != arr[j]:
            arr[i], arr[j] = arr[j], arr[i]
        else:
            duplicates.append(arr[i])
            i += 1
    else:
        i += 1

print(duplicates)