arr = [3, 1, 5, 4, 2]

i = 0
while i < len(arr):
    j = arr[i] - 1
    if arr[i] != arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        i += 1

print(arr)
