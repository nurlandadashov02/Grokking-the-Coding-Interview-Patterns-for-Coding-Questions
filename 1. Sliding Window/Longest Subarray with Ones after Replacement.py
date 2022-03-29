array = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k = 2

window_start = 0
max_length = 0
max_count = 0
dict = {}

for window_end in range(len(array)):
    el = array[window_end]
    if el not in dict:
        dict[el] = 0
    dict[el] += 1

    max_count = max(max_count, dict[el])

    while window_end - window_start + 1 - max_count > k:
        dict[array[window_start]] -= 1
        window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
