import math

inp = [3, 4, 1, 1, 6]
S = 8

min_length = math.inf
window_end = 0
window_start = 0
_sum = 0

while window_end < len(inp):
    _sum += inp[window_end]

    while _sum >= S:
        min_length = min(min_length, window_end - window_start + 1)
        _sum -= inp[window_start]
        window_start += 1

    window_end += 1

if min_length == math.inf:
    min_length = 0

print(min_length)
