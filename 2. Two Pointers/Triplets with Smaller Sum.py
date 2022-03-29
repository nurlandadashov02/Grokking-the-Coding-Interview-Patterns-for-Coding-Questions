inp = [-1, 4, 2, 1, 3]
target = 5
n = len(inp)
inp = sorted(inp)

count = 0

for i in range(n):
    if i > 0 and inp[i] == inp[i - 1]:
        continue

    left, right = i + 1,  n - 1
    target_sum = target - inp[i]

    while left < right:
        if inp[left] + inp[right] + inp[i] < target:
            count += right - left
            left += 1
        else:
            right -= 1


print(count)