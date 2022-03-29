arr = [1, 1, 2, 2]


def subsets(nums):
    nums.sort()
    res = [[]]
    end = 0
    for i in range(len(nums)):
        num = nums[i]
        start = 0
        if i > 0 and num == nums[i - 1]:
            start = end + 1
        n = len(res)
        end = n - 1
        for j in range(start, n):
            res.append(res[j] + [num])

    return res


print(subsets(arr))
