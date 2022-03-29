arr = [2, 3, 1, 8, 2, 3, 5, 1]

i = 0
while i < len(arr):
    j = arr[i] - 1
    if arr[i] != arr[j]:
        arr[i], arr[j] = arr[j], arr[i]
    else:
        i += 1

missing = []
for i in range(len(arr)):
    if arr[i] != i + 1:
        missing.append(i + 1)

print(missing)
