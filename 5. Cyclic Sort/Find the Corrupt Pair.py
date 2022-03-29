arr = [3, 1, 2, 3, 6, 4]

i = 0
while i < len(arr):
    j = arr[i] - 1
    if arr[i] != arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        i += 1

for i in range(len(arr)):
    if arr[i] != i + 1:
        print([arr[i], i + 1])