arr = [4, 1, 2, -1, 1, -3]
arr.sort()
target = 1

n = len(arr)
quadruplets = []

for first in range(0, n - 3):
    if first > 0 and arr[first] == arr[first - 1]:
        continue
    for second in range(first + 1, n - 2):
        if second > first + 1 and arr[second] == arr[second - 1]:
            continue

        target_sum = target - (arr[first] + arr[second])
        low, high = second + 1, n - 1

        while low < high:
            current_sum = arr[low] + arr[high]
            if current_sum > target_sum:
                high -= 1
            elif current_sum < target_sum:
                low += 1
            else:
                quadruplets.append([arr[first], arr[second], arr[low], arr[high]])
                low += 1
                high -= 1
                while low < high and arr[low] == arr[low - 1]:
                    low += 1
                while low < high and arr[high] == arr[high + 1]:
                    high -= 1


print(quadruplets)