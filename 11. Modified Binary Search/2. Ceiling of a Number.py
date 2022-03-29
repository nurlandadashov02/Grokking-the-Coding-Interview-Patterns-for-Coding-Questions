nums = [4, 6, 10]
target = 5

def ceil(nums, target):
    low, mid, high = 0, 0, len(nums) - 1

    while low <= high:
        mid = (low + high) // 2

        if nums[mid] < target:
            low = mid + 1
        elif nums[mid] > target:
            high = mid - 1
        else:
            break

    if (mid == 0 and nums[mid] > target) or (mid == len(nums) - 1 and nums[mid] < target):
        return -1
    elif nums[mid] < target:
        return mid + 1
    else:
        return mid

print(ceil(nums, target))