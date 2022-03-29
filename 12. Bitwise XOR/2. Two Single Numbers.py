nums = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]

x = nums[0]

for i in range(1, len(nums)):
    x ^= nums[i]

bit = 1
while (bit & x) == 0:
    bit = bit << 1

num1, num2 = 0, 0

for num in nums:
    if (num & bit) != 0:
        num1 ^= num
    else:
        num2 ^= num

print([num1, num2])
