from collections import deque

arr = [1, 3, 5]

def permutate(nums):
    res = [[nums[0]]]
    for i in range(1, len(nums)):
        arr = []
        for per in res:
            for k in range(i + 1):
                l = deque(per)
                l.insert(k, nums[i])
                arr.append(l)

        res = arr

    return [list(r) for r in res]



print(permutate(arr))