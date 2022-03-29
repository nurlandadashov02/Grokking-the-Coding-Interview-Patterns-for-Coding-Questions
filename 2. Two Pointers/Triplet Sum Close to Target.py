import math

inp = [-2, 0, 1, 2]
target = 2
n = len(inp)
inp = sorted(inp)

close_sum = 0

for i in range(n):
    if i > 0 and inp[i] == inp[i - 1]:
        continue

    left, right = i + 1,  n - 1
    target_sum = target - inp[i]
    match_sum = -math.inf

    while left < right:
        current_sum = inp[left] + inp[right]
        if abs(target - match_sum) > abs(target - (current_sum + inp[i])):
            match_sum = current_sum + inp[i]

        if current_sum > target_sum:
            right -= 1
        elif current_sum < target_sum:
            left += 1
        else:
            break

    if abs(target - match_sum) < abs(target - close_sum):
        close_sum = match_sum


print(close_sum)