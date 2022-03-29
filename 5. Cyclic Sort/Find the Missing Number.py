arr = [8, 3, 5, 2, 4, 6, 0, 1]

i = 0
while i < len(arr):
    j = arr[i]
    if arr[i] < len(arr) and arr[i] != arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        i += 1

for i in range(len(arr)):
    if arr[i] != i:
        print(i)
        break
