inp = [2, 1, 5, 1, 3, 2]
k = 3

_sum = 0
for j in range(k):
    _sum += inp[j]

maxSum = _sum

for i in range(1, len(inp) - k + 1):
    _sum -= inp[i - 1]
    _sum += inp[i + k - 1]
    if _sum > maxSum:
        maxSum = _sum

print(maxSum)