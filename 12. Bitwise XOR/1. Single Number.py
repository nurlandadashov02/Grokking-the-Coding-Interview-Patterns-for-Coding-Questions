nums = [7, 9, 7]

x = nums[0]
for i in range(1, len(nums)):
    x ^= nums[i]

print(x)
