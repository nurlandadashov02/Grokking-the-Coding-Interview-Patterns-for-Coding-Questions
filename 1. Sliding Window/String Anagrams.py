string = "abbcabc"
pattern = "abc"

dict_pattern = {}

for c in pattern:
    if c not in dict_pattern:
        dict_pattern[c] = 0
    dict_pattern[c] += 1

window_start = 0

indices = []
matched = 0
for window_end in range(len(string)):
    if string[window_end] in dict_pattern:
        dict_pattern[string[window_end]] -= 1
        if dict_pattern[string[window_end]] == 0:
            matched += 1
    if matched == len(dict_pattern):
        indices.append(window_start)

    if window_end >= len(pattern) - 1:
        if string[window_start] in dict_pattern:
            if dict_pattern[string[window_start]] == 0:
                matched -= 1
            dict_pattern[string[window_start]] += 1
        window_start += 1

print(indices)