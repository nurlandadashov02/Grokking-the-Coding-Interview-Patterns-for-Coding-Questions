string = "aabccbb"

window_start = 0
max_length = 0
char = set()

for window_end in range(len(string)):
    while string[window_end] in char:
        char.remove(string[window_start])
        window_start += 1

    char.add(string[window_end])
    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
