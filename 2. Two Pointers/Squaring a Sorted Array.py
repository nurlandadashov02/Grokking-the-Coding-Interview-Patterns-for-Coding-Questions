inp = [-2, -1, 0, 2, 3]
n = len(inp)

left, right = 0, n - 1
highestIdx = n - 1
arr = [0 for x in range(n)]

while left <= right:
    if abs(inp[left]) > inp[right]:
        arr[highestIdx] = inp[left] ** 2
        left += 1
    else:
        arr[highestIdx] = inp[right] ** 2
        right -= 1

    highestIdx -= 1

print(arr)

