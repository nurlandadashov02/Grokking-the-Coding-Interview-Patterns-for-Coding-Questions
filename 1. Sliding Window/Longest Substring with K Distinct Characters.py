string = "araaci"
k = 2

window_start = 0
max_length = 0
char = {}

for window_end in range(len(string)):
    if string[window_end] not in char:
        char[string[window_end]] = 1
    else:
        char[string[window_end]] += 1

    while len(char) > k:
        char[string[window_start]] -= 1
        if char[string[window_start]] == 0:
            del char[string[window_start]]
        window_start += 1

    max_length = max(max_length, window_end - window_start + 1)

print(max_length)
