nums = ['a', 'c', 'f', 'h']
target = '.'

def ceil(nums, target):
    low, mid, high = 0, 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            mid += 1
            break

    if mid == 0 and nums[mid] > target:
        return nums[-1]
    elif (mid == len(nums) - 1 and nums[mid] < target) or mid == len(nums):
        return nums[0]
    elif nums[mid] < target:
        return nums[mid + 1]
    else:
        return nums[mid]

print(ceil(nums, target))