inp = [-3, 0, 1, 2, -1, 1, -2]
n = len(inp)
inp = sorted(inp)

triplets = []

for i in range(n):
    if i > 0 and inp[i] == inp[i - 1]:
        continue

    left, right = i + 1,  n - 1
    target = -inp[i]

    while left < right:
        current_sum = inp[left] + inp[right]
        if current_sum > target:
            right -= 1
        elif current_sum < target:
            left += 1
        else:
            triplets.append([inp[i], inp[left], inp[right]])
            left += 1
            right -= 1
            while left < right and inp[left] == inp[left - 1]:
                left += 1
            while left < right and inp[right] == inp[right + 1]:
                right -= 1


print(triplets)