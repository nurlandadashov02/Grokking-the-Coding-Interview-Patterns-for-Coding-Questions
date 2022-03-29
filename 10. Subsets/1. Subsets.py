from collections import deque

arr = [1, 5, 3]

def subsets(nums):
    res = [[]]

    for num in nums:
        n = len(res)
        for i in range(n):
            res.append(res[i] + [num])

    return res

print(subsets(arr))