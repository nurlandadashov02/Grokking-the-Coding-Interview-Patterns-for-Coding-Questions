from sortedcontainers import SortedList

nums = [1, 2, -1, 3, 5]
k = 2

res = []
arr = SortedList(nums[:k])

m1, m2 = k // 2 - 1, k // 2
for i in range(k, len(nums)):
    if k % 2 == 0:
        res.append((arr[m1] + arr[m2]) / 2.0)
    else:
        res.append(arr[m2])
    arr.remove(nums[i - k])
    arr.add(nums[i])

if k % 2 == 0:
    res.append((arr[m1] + arr[m2]) / 2.0)
else:
    res.append(arr[m2])

print(res)